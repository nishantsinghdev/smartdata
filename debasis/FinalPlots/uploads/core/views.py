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
from uploads.core import outliers as out
from uploads.core import heatMap as heat
from uploads.core import stats as st
from uploads.core import categorical as cat

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
    outlierspath = os.path.join(my_path, 'static/images/outliers')
    hitmappath = os.path.join(my_path, 'static/images/hitmap')
    statisticspath = os.path.join(my_path, 'static/images/statistics')
    categoricalspath = os.path.join(my_path, 'static/images/categorical')

    box = os.listdir(boxpath)
    dist = os.listdir(distpath)
    scatter = os.listdir(scatterpath)
    outlier = os.listdir(outlierspath)
    heatmap = os.listdir(hitmappath)
    statistics = os.listdir(statisticspath)
    categorical = os.listdir(categoricalspath)

    boxlist = list()
    for filename in box:
        boxlist.append(str('/static/images/box/' + filename))

    distlist = list()
    for filename in dist:
        distlist.append(str('/static/images/distplot/' + filename))

    scatterlist = list()
    for filename in scatter:
        scatterlist.append(str('/static/images/scatter/' + filename))

    outlierlist = list()
    for filename in outlier:
        outlierlist.append(str('/static/images/outliers/' + filename))

    heatmaplist = list()
    for filename in heatmap:
        heatmaplist.append(str('/static/images/hitmap/' + filename))

    statisticslist = list()
    for filename in statistics:
        statisticslist.append(str('/static/images/statistics/' + filename))

    categoricallist = list()
    for filename in categorical:
        categoricallist.append(str('/static/images/categorical/' + filename))

    context = {
        'l1': boxlist,
        'l2': distlist,
        'l3': scatterlist,
        'l4': outlierlist,
        'l5': heatmaplist,
        'l6': statisticslist,
        'l7': categoricallist,

    }
    #print(heatmaplist)
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

        out.outliers(path)
        #####call outliers

        st.stats(path)

        heat.heat_map(path)
        cat.catg(path)


        #### Creating PDF
        pg.generate()
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
    cl.cleanPdf()
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
