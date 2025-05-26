from django.urls import path
from . import views

app_name = "leads"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.lead_detail, name="lead_detail"),
    path("create/", views.lead_create, name="lead_create"),
]
