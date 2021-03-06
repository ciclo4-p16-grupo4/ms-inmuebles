from django.contrib import admin
from django.urls import path, re_path
from inmueblesApp import views as inmueblesAppViews

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^inmuebles/$', inmueblesAppViews.ImnueblesAllView.as_view()),
    re_path(r'^inmuebles/search$', inmueblesAppViews.ImnuebleSearch().as_view()),
    path('inmuebles/<int:pk>/', inmueblesAppViews.InmueblesDetailView.as_view()), #shows Inmuebles details
    path('inmuebles/create/', inmueblesAppViews.InmueblesCreateView.as_view()), #add a product to the db
    path('inmuebles/update/<int:id>/', inmueblesAppViews.InmueblesUpdateView.as_view()), #updates a product from the database
    path('inmuebles/delete/<int:id>/', inmueblesAppViews.InmueblesDeleteView.as_view()), #delete a product from the database
]
