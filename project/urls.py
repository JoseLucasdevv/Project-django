from django import views
from django.contrib import admin
from django.urls import path
from website.views import form, create, home
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "form/",
        form,
        name="form",
    ),
    path("create/", create, name="create"),
    path("", home, name="home"),
]
