from xml.dom.minidom import Document
import django
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('' , include('BlogApp.urls')),
    path('course/' , include('courses_app.urls')),
    path('account/',include('BlogApp.urls'))
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


