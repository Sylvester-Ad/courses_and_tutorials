"""
URL configuration for djcrm project.
"""
from django.contrib import admin
from django.urls import path, include
from leads.views import LandingPageView, SignUpView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", LandingPageView.as_view(), name="landing_page"),
    path('leads/', include("leads.urls"), name="leads"),
    path('agents/', include("agents.urls"), name="agents"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
