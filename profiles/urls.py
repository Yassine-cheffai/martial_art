from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.MyHomeView.as_view(), name='my_home'),
    path('<int:user_id>/home/', views.VisitingHomeView.as_view(), name='visit_home'),
]
