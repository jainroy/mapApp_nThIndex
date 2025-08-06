from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mapplaces.urls')),
    path('', include('mapplaces.urls')),  # So '/map/' works
]
