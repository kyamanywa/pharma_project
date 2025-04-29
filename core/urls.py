from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),  # Root URL now points to the dashboard
    path('login/', views.login_view, name='login'),
    path('report/', views.product_report_view, name='product_report'),
    path('production_report/', views.production_report, name='production_report'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
