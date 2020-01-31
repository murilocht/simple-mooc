from django.contrib import admin
from django.urls import path, include
from simplemooc.core import urls

urlpatterns = [
    path('', include(urls, namespace='core')),
    path('admin/', admin.site.urls),
]
