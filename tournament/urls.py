from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from .views import TournmentsTableView
urlpatterns = [
    # path('', MyHomeView.as_view(), name='index'),
    path('',TournmentsTableView.as_view(),name='tournments_list'),

]
