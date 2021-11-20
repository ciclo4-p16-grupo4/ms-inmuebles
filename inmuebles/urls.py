from django.contrib import admin
from django.urls import path
from inmueblesApp import views as inmueblesAppViews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inmuebles/<int:pk>/', inmueblesAppViews.InmueblesDetailView.as_view()), #shows Inmuebles details
    path('inmuebles/create/', inmueblesAppViews.InmueblesCreateView.as_view()), #add a product to the db
    path('inmuebles/update/<int:id>/', inmueblesAppViews.InmueblesUpdateView.as_view()), #updates a product from the database
    path('inmuebles/delete/<int:id>/', inmueblesAppViews.InmueblesDeleteView.as_view()), #delete a product from the database
]
