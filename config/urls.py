from django.urls import path
from timetable import views
urlpatterns = [path('', views.weekly, name='weekly'), path('add/', views.edit, name='add'), path('<int:pk>/', views.detail, name='detail'), path('<int:pk>/edit/', views.edit, name='edit'), path('<int:pk>/delete/', views.delete, name='delete')]
