from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('interior/', include('interior.urls')),
    path('', RedirectView.as_view(url='interior/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
]