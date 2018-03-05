import os.path
from reportlab.pdfgen import canvas


def generate():
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    spath1 = os.path.join(my_path, 'static\\images\\box\\')
    spath2 = os.path.join(my_path, 'static\\images\\distplot\\')
    spath3 = os.path.join(my_path, 'static\\images\\scatter\\')

    box = os.listdir(spath1)
    dist = os.listdir(spath2)
    scatter = os.listdir(spath3)



    ###changing the save file path
    pdf = os.path.join(my_path, 'static\\pdfs\\')
    c = canvas.Canvas(pdf + 'AllPlots.pdf')
    #print(list)
    y = 400
    ####adding box plots
    for x in box:
        img = os.path.join(spath1 + x)
        c.drawImage(img, 0, y, 420, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400

    ####adding dist plots
    for x in dist:
        img = os.path.join(spath2 + x)
        c.drawImage(img, 0, y, 420, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400

    ####adding scatter plots
    for x in scatter:
        img = os.path.join(spath3 + x)
        c.drawImage(img, 0, y, 420, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400
    ##generate in a specified directory
    #c.drawImage('D:\\githubLOCAL\\smartdata\\debasis\\Updated-StaticFile\\static\\images\\figure1.png', 10, 10, 450, 180)
    c.save()
generate()




