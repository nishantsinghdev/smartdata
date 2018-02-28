from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os.path
from uploads.core.models import Document
from uploads.core.forms import DocumentForm
from uploads.core import testdemo as tst
from uploads.core import ssd_scatterplott as ss
from uploads.core import BoxPlot as box
from uploads.core import clean as cl

def home(request):
    ### get all the files from documents
    documents = Document.objects.all()
    #print(Document.uploaded_at)
    return render(request, 'core/home.html', {'documents': documents})

### Display all plots
def display(request):
    import os.path
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    spath = os.path.join(my_path, 'static/images')
    imglist = os.listdir(spath)
    newlist = list()
    for filename in imglist:
        i = str('/static/images/'+filename)
        newlist.append(i)
    context = {
        'list': newlist,
    }
    #print(list)
    return render(request, 'core/images.html', context)

### Generates plots
def invoke(request):

    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    spath = os.path.join(my_path, 'documents')
    list = os.listdir(spath)
    leng = list.__len__()
    if leng == 0:
        return render(request, 'core/noData.html')
    else:
        get = list[0]
        path = os.path.join(my_path + '\documents' + '\\' + get)


        tst.scatter(path)
        #creates Scatter Plots

        ss.histo(path)
        #creates dist plot

        box.box(path)
        #creates boxplot
        #return render(request, 'core/images.html')
        return redirect(display)  #### redirects to display method......


def model_form_upload(request):
    cl.cleanDoc()
    cl.cleanImg()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })