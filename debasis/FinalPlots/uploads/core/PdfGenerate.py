import os.path
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def generate():
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    spath1 = os.path.join(my_path, 'static\\images\\box\\')
    spath2 = os.path.join(my_path, 'static\\images\\distplot\\')
    spath3 = os.path.join(my_path, 'static\\images\\scatter\\')
    spath4 = os.path.join(my_path, 'static\\images\\outliers\\')

    box = os.listdir(spath1)
    dist = os.listdir(spath2)
    scatter = os.listdir(spath3)
    outliers = os.listdir(spath4)

    ###changing the save file path
    pdf = os.path.join(my_path, 'static\\pdfs\\')
    ####pdf name is hardcoaded
    c = canvas.Canvas(pdf + 'AllPlots.pdf')

    #print(list)
    y = 400
    ####adding box plots
    c.setFont("Helvetica", 30)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(250, 770, "Box Plots")
    for x in box:
        img = os.path.join(spath1 + x)
        c.drawImage(img, 0, y, 420, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400

    ####adding dist plots
    c.setFont("Helvetica", 30)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(250, 770, "Dist Plots")
    for x in dist:
        img = os.path.join(spath2 + x)
        c.drawImage(img, 0, y, 420, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400

    ####adding scatter plots
    c.setFont("Helvetica", 30)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(250, 770, "Scatter Plots")
    for x in scatter:
        img = os.path.join(spath3 + x)
        c.drawImage(img, 0, y, 420, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400

    ####adding outliers plots
    c.setFont("Helvetica", 30)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(250, 770, "Outliers")
    for x in outliers:
        img = os.path.join(spath4 + x)
        c.drawImage(img, 0, y, 420, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400

    ##generate in a specified directory
    #c.drawImage('D:\\githubLOCAL\\smartdata\\debasis\\Updated-StaticFile\\static\\images\\figure1.png', 10, 10, 450, 180)
    c.save()
#generate()




