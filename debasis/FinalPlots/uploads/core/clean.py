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
    files1 = os.listdir(p1)
    files2 = os.listdir(p2)
    files3 = os.listdir(p3)
    #print(spath)
    for f in files1:
        os.remove(os.path.join(p1, f))
    for f in files2:
        os.remove(os.path.join(p2, f))
    for f in files3:
        os.remove(os.path.join(p3, f))
#cleanImg()

def cleanPdf():
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    spath = os.path.join(my_path, 'static/pdfs')
    files = os.listdir(spath)
    #print(spath)
    for f in files:
        os.remove(os.path.join(spath, f))
#cleanPdf()
