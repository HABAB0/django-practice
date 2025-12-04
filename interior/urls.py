from django.urls import path
from interior import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('profile/registration', views.registration, name='registration'),
    path('applications/create/', views.createApplication, name='createApplication'),
    path('applications/', views.ApplicationList.as_view(), name='applicationList'),
    path('applications/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='applicationDelete'),
    path('applications/<int:pk>/update/', views.ApplicationUpdate.as_view(), name='applicationUpdate'),
    path('applications/all/', views.AllApplications.as_view(), name='allApplications'),
    path('categories/create/', views.CategoryCreate.as_view(), name='categoryCreate'),
    path('categories/', views.AllCategory.as_view(), name='categoryList'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='categoryDelete'),
]