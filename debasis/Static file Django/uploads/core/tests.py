import os.path

my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
spath = os.path.join(my_path, 'documents')
list = os.listdir(spath)
get = list.__len__()
#print(get)
if get == 0:
    print("data is not present")
else:
    print("data is present")