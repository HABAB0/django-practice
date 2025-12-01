from django.urls import path
from interior import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:pk>', views.Profile.as_view(), name='profile'),
    path('profile/registration', views.Registration.as_view(), name='registration'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)