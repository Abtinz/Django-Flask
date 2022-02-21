from django.contrib import admin
from django.urls import path,include

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('' , include('BlogApp.urls')),
    path('account/',include('BlogApp.urls'))
]


