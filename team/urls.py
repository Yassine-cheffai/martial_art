from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import TeamsList


urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path('teams/', TeamsList.as_view(), name="teams"),
    path('teams/add/', views.add_team, name="add_team"),
    path('competitor', views.add_competitor, name="add_competitor")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
