from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from uploads.core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^uploads/simple/$', views.display, name='simple_upload'),
    url(r'^uploads/invoke/$', views.invoke, name='invoke'),
    url(r'^uploads/ssd/$', views.ssd, name='ssd'),
    url(r'^uploads/boxplot/$', views.boxplot, name='boxplot'), #in the home.html on click boxplot it will call views.boxplot
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



