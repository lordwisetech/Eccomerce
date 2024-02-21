
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from app import views
from .views import *
urlpatterns = [
    path("home/",home.as_view(), name="home"),
    path('store/<str:slug>', views.store, name="store"),
    path('store/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path("",views.register, name="register"),
    path('login-user',views.login, name="login" )


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
