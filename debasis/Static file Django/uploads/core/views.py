from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os.path
from uploads.core.models import Document
from uploads.core.forms import DocumentForm
from uploads.core import testdemo as tst
from uploads.core import ssd_scatterplott as ss
from uploads.core import BoxPlot as box

def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def display(request):
    import os.path
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    spath = os.path.join(my_path, 'static/images')
    imglist = os.listdir(spath)
    newlist = list()
    for filename in imglist:
        newlist.append('/static/images/'+filename)
    context = {
        'list': newlist,
    }
    print(list)
    return render(request, 'core/images.html', context)

def invoke(request):
    path = 'C:\\Users\\Debasis Pramanik\\Desktop\\Ecommerce Purchases.csv'
    tst.scatter(path)
    return render(request, 'core/done.html')

def ssd(request):
    path = 'C:\\Users\\Debasis Pramanik\\Desktop\\Ecommerce Purchases.csv'
    ss.histo(path)
    return render(request, 'core/done.html')

def boxplot(request):
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    path = os.path.join(my_path, 'documents/Ecommerce_Purchases.csv')
    box.box(path)
    return render(request, 'core/done.html')



def model_form_upload(request):
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
