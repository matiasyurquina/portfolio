
from django.contrib import admin
from django.urls import path
from portfolio import views
handler404 = 'portfolio.views.error_404'
handler500 = 'portfolio.views.error_500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('es/', views.homeES, name="homeES"),
    path('pt/', views.homePT, name="homePT"),
    path('contact/', views.contact, name='contact'),
]
