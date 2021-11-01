from django.urls import path, include
from stipendiya import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', include('dashboard.urls'))


]
