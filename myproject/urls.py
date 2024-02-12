from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_trade, name='add_trade'),
    path('update/<int:pk>/', views.update_trade, name='update_trade'),
    path('delete/<int:pk>/', views.delete_trade, name='delete_trade'),
    #path('chart/', views.chart_view, name='chart_view'),
    path('visualize/', views.visualize_data, name='visualize_data'),
    path('contact/', views.contact, name='about me'),
    path('projectdescribe/', views.about_project, name='about me'),
    path('admin/', admin.site.urls),
]
