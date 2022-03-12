from django.urls import path
from . import views
from django.contrib import admin

#address list
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home) ,
    path("contact",views.contact),
    path("signUp",views.new_account),
    path("profile/<username>",views.account),
]