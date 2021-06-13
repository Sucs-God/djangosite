"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SectionsViewIndex.as_view(), name='main'),
    path('about/', views.about, name='about'),
    path('catalog/', views.SectionsViewCatalog.as_view(), name='catalog'),
    path('catalog/<slug:section>/', views.BooksView.as_view(), name='section_url'),
    path('catalog/<slug:section>/<slug:slug>/', views.BookDetailView.as_view(), name='book_detail'),
]
