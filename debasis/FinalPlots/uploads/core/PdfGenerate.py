import os.path
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def generate():
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    spath1 = os.path.join(my_path, 'static\\images\\box\\')
    spath2 = os.path.join(my_path, 'static\\images\\distplot\\')
    spath3 = os.path.join(my_path, 'static\\images\\scatter\\')
    spath4 = os.path.join(my_path, 'static\\images\\outliers\\')
    spath5 = os.path.join(my_path, 'static\\images\\hitmap\\')
    spath6 = os.path.join(my_path, 'static\\images\\statistics\\')
    spath7 = os.path.join(my_path, 'static\\images\\categorical\\')

    box = os.listdir(spath1)
    dist = os.listdir(spath2)
    scatter = os.listdir(spath3)
    outliers = os.listdir(spath4)
    hitmap = os.listdir(spath5)
    statistics = os.listdir(spath6)
    categorical = os.listdir(spath7)

    ###changing the save file path
    pdf = os.path.join(my_path, 'static\\pdfs\\')
    ####pdf name is hardcoaded
    c = canvas.Canvas(pdf + 'AllPlots.pdf')

    #print(list)
    y = 450
    ####adding box plots
    c.setFont("Helvetica", 30)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(250, 770, "Box Plots")
    for x in box:
        img = os.path.join(spath1 + x)
        c.drawImage(img, 0, y, 400, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400
    if box.__len__()%2==0 & box.__len__()==1:
        print()
    else:
        c.showPage()
        y = 450
    ####adding dist plots
    c.setFont("Helvetica", 30)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(250, 770, "Dist Plots")
    for x in dist:
        img = os.path.join(spath2 + x)
        c.drawImage(img, 0, y, 400, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400
    if box.__len__()%2==0 & box.__len__()==1:
        print()
    else:
        c.showPage()
        y = 450
    ####adding scatter plots
    c.setFont("Helvetica", 30)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(250, 770, "Scatter Plots")
    for x in scatter:
        img = os.path.join(spath3 + x)
        c.drawImage(img, 0, y, 400, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400
    if box.__len__()%2==0 & box.__len__()==1:
        print()
    else:
        c.showPage()
        y = 450

    ####adding outliers plots
    c.setFont("Helvetica", 30)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(250, 770, "Outliers")
    for x in outliers:
        img = os.path.join(spath4 + x)
        c.drawImage(img, 0, y, 400, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400
    if box.__len__()%2==0 & box.__len__()==1:
        print()
    else:
        c.showPage()
        y = 450

    ####adding hitmap plots
    c.setFont("Helvetica", 30)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(250, 770, "hitmap")
    for x in hitmap:
        img = os.path.join(spath5 + x)
        c.drawImage(img, 0, y, 400, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400
    if box.__len__()%2==0 & box.__len__()==1:
        print()
    else:
        c.showPage()
        y = 450

    ####adding statistics plots
    c.setFont("Helvetica", 30)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(250, 770, "statistics")
    for x in statistics:
        img = os.path.join(spath6 + x)
        c.drawImage(img, 0, y, 400, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400
    if box.__len__()%2==0 & box.__len__()==1:
        print()
    else:
        c.showPage()
        y = 450
    ####adding categorical plots
    c.setFont("Helvetica", 30)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(250, 770, "categorical")
    for x in categorical:
        img = os.path.join(spath7 + x)
        c.drawImage(img, 0, y, 400, 300)
        y = y-350
        if y <= 0:
            c.showPage()
            y=400
    ##generate in a specified directory
    #c.drawImage('D:\\githubLOCAL\\smartdata\\debasis\\Updated-StaticFile\\static\\images\\figure1.png', 10, 10, 450, 180)
    c.save()
generate()




