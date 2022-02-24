from django.urls import path
from . import views
from django.contrib import admin

#address list
urlpatterns = [
    path('admin/', admin.site.urls),
    path("courses/list",views.courses_list),
    path("information/<int:course_id>",views.course_information)
]