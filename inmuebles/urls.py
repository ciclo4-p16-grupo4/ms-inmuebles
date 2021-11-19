from django.contrib import admin
from django.urls import path
from inmueblesApp import views as inmueblesAppViews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()), # use credentials to return tokens
    path('refresh/',TokenRefreshView.as_view()), # generate new access token
    path('verifyToken/', inmueblesAppViews.VerifyTokenView.as_view()),
    path('user/', inmueblesAppViews.UserCreateView.as_view()), # create a new user
    path('user/<int:pk>/', inmueblesAppViews.UserDetailView.as_view()), # check info for an specific user based on id(pk)

    path('inmuebles/<int:pk>/', inmueblesAppViews.InmueblesDetailView.as_view()), #shows Inmuebles details
    path('inmuebles/create/', inmueblesAppViews.InmueblesCreateView.as_view()), #add a product to the db
    path('inmuebles/update/<int:pk>/', inmueblesAppViews.InmueblesUpdateView.as_view()), #updates a product from the database
    path('inmuebles/delete/<int:pk>/', inmueblesAppViews.InmueblesDeleteView.as_view()), #delete a product from the database
]
