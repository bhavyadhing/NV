
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from college import views

urlpatterns = [
    path('home/', views.home),
    path('notice/', views.NoticeListView.as_view()),
    path('notice/<int:pk>',  views.NoticeDetailView.as_view()),
    path('', RedirectView.as_view(url='home/')),
]
