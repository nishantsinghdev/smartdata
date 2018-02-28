import os.path

my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
spath = os.path.join(my_path, 'static/images/boxplot')
l = os.listdir(spath)
print(l)
context = {
    'list': l,
}
for img in l:
    print(type(img))
