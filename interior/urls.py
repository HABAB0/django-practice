from django.urls import path
from interior import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/registration', views.registration, name='registration'),
    path('applications/create/', views.createApplication, name='createApplication'),
    path('applications/', views.ApplicationList.as_view(), name='applicationList'),
    path('applications/<int:pk>', views.ApplicationDelete.as_view(), name='applicationDelete'),
    path('applications/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='applicationDelete'),
]