
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("",include("core.urls")),
    path('accounts/', include('allauth.urls')),  # Allauth handles everything
    path('admin/', admin.site.urls),
    
]
