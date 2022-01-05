from django.urls import path

from .views import ClassView, aboutView, homePageView

urlpatterns=[
    path('',homePageView,name='home'),
    path('xyz/',ClassView.as_view(),name='classview'),
    path('about/',aboutView,name='about')
]