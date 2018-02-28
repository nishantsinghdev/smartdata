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
    spath = os.path.join(my_path, 'static/images')
    files = os.listdir(spath)
    #print(spath)
    for f in files:
        os.remove(os.path.join(spath, f))
#cleanImg()