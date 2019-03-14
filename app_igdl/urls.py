from django.urls import path
from . import views


app_name = 'app_igdl'
urlpatterns = [
	path('', views.download, name='download'),
	path('image/', views.image, name='image'),
]
