from django.urls import path
from . import views

app_name = "leads"
urlpatterns = [
    path("", views.LeadIndexView.as_view(), name="index"),
    path("<int:pk>/", views.LeadDetailView.as_view(), name="lead_detail"),
    path("<int:pk>/update/", views.LeadUpdateView.as_view(), name="lead_update"),
    path("<int:pk>/delete/", views.LeadDeleteView.as_view(), name="lead_delete"),
    path("create/", views.LeadCreateView.as_view(), name="lead_create"),
    path("<int:pk>/assign_agent", views.AssignAgentView.as_view(), name="assign_agent"),
]
