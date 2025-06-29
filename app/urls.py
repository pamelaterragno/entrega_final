from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.PostListView.as_view(), name='list'),  # Cambiado a CBV
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('sobremi/', views.about_me, name='sobremi'),
    path('create/', views.create_post, name='crear'),
    path('edit/<int:post_id>/', views.edit_post, name='edit'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
    path('perfil/', views.perfil, name='perfil'),
    path('profile/', views.profile, name='profile'),
]
