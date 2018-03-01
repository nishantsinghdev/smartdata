import os.path
from reportlab.pdfgen import canvas


def generate():
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    spath = os.path.join(my_path, 'static\\images\\')
    print(spath)
    list = os.listdir(spath)

    ###changing the save file path
    spath1 = os.path.join(my_path, 'static\\pdfs\\')
    c = canvas.Canvas(spath1 + 'AllPlots.pdf')
    #print(list)
    y = 400
    for x in list:
        img = os.path.join(spath + x)
        c.drawImage(img, 0, y, 420, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400

    ##generate in a specified directory
    #c.drawImage('D:\\githubLOCAL\\smartdata\\debasis\\Updated-StaticFile\\static\\images\\figure1.png', 10, 10, 450, 180)
    c.save()
generate()




