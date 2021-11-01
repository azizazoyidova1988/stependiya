from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('talaba/list/', views.talaba_list, name="talaba_list"),
    path('talaba/add/', views.talaba_create, name="talaba_add"),

    path('otm/list/', views.otm_list, name="otm_list"),
    path('otm/add/', views.otm_create, name="otm_add"),

    path('adminstrator/list/', views.adminstrator_list, name="adminstrator_list"),
    path('adminstrator/add/', views.adminstrator_create, name="adminstrator_add"),


    path('talaba_faoliyati/list/', views.talaba_faoliyati_list, name="talaba_faoliyati_list"),

    path('talaba_xisoboti/list/', views.talaba_xisoboti_list, name="talaba_xisoboti_list"),

    path('yangi_ariza/list/', views.yangi_ariza_list, name="yangi_ariza_list"),

    path("status/<int:pk>/<int:status>", views.status, name="status"),

    path('status/list/', views.ariza_status_list, name='ariza_status_list'),


   ]