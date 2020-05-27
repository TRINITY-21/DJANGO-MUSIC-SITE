from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('album/add/', views.AlbumCreate.as_view(), name='album_add'),

    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album_update'),

    path('album/<int:pk>/delete', views.AlbumDelete.as_view(), name='album_delete'),

    path('register/', views.UserFormView.as_view(), name='register'),

]