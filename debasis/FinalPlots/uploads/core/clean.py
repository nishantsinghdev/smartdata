import os.path
#### Clean Documents
def cleanDoc():
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    spath = os.path.join(my_path, 'documents')
    files = os.listdir(spath)
    #print(spath)
    for f in files:
        os.remove(os.path.join(spath, f))

#clean()
#### Clean Images
def cleanImg():
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    p1 = os.path.join(my_path, 'static/images/box/')
    p2 = os.path.join(my_path, 'static/images/distplot/')
    p3 = os.path.join(my_path, 'static/images/scatter/')
    p4 = os.path.join(my_path, 'static/images/outliers/')
    p5 = os.path.join(my_path, 'static/images/statistics/')
    p6 = os.path.join(my_path, 'static/images/hitmap/')
    p7 = os.path.join(my_path, 'static/images/categorical/')
    files1 = os.listdir(p1)
    files2 = os.listdir(p2)
    files3 = os.listdir(p3)
    files4 = os.listdir(p4)
    files5 = os.listdir(p5)
    files6 = os.listdir(p6)
    files7 = os.listdir(p7)
    #print(spath)
    for f in files1:
        os.remove(os.path.join(p1, f))
    for f in files2:
        os.remove(os.path.join(p2, f))
    for f in files3:
        os.remove(os.path.join(p3, f))
    for f in files4:
        os.remove(os.path.join(p4, f))
    for f in files5:
        os.remove(os.path.join(p5, f))
    for f in files6:
        os.remove(os.path.join(p6, f))
    for f in files7:
        os.remove(os.path.join(p7, f))
#cleanImg()

def cleanPdf():
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    spath = os.path.join(my_path, 'static/pdfs')
    files = os.listdir(spath)
    #print(spath)
    for f in files:
        os.remove(os.path.join(spath, f))
#cleanPdf()
