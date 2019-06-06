"""modledemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from modle.views import goindex,addBook,queryBook,queryBookById,deleteBook,updateBookById,getTest,getFilter,SqlTest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',goindex),
    path('addBook/',addBook),
    path('queryBook/',queryBook),
    path('queryBookByIdGet/',queryBookById),
    path('deleteBookById/<int:id>/',deleteBook),
    path('updateBookById/<int:id>/<str:name>/',updateBookById),
    path('gettest/',getTest),
    path('filtertest/',getFilter),
    path('sqltest/',SqlTest),
]
