from django.http import Http404, HttpResponse
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
from uploads.core import PdfGenerate as pg

def home(request):
    ### get all the files from documents
    documents = Document.objects.all()
    #print(Document.uploaded_at)
    return render(request, 'core/home.html', {'documents': documents})

### Display all plots
def display(request):
    import os.path
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    boxpath = os.path.join(my_path, 'static/images/box')
    distpath = os.path.join(my_path, 'static/images/distplot')
    scatterpath = os.path.join(my_path, 'static/images/scatter')

    box = os.listdir(boxpath)
    dist = os.listdir(distpath)
    scatter = os.listdir(scatterpath)
    boxlist = list()
    for filename in box:
        i = str('/static/images/box/'+filename)
        boxlist.append(i)
    distlist = list()
    for filename in dist:
        i = str('/static/images/distplot/' + filename)
        distlist.append(i)
    scatterlist = list()
    for filename in scatter:
        i = str('/static/images/scatter/' + filename)
        scatterlist.append(i)

    context = {
        'l1': boxlist,
        'l2': distlist,
        'l3': scatterlist,
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

        #### Creating PDF
        #pg.generate()
        #return render(request, 'core/images.html')
        return redirect(display)  #### redirects to display method......

######download PDF
def download(request):
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    spath1 = os.path.join(my_path, 'static\\pdfs\\AllPlots.pdf')
    if os.path.exists(spath1):
        with open(spath1, 'rb') as fh:
            response = HttpResponse(fh.read())
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(spath1)
            return response
    raise Http404


def model_form_upload(request):
    cl.cleanDoc()
    cl.cleanImg()
    #cl.cleanPdf()
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
