from django.urls import path
from .views import home_view, login_view, post_list, post_create, post_detail, logout_view

urlpatterns = [
    path('', home_view, name='home'),  # Home page (login page)
    path('login/', login_view, name='login'),  # Login page
    path('posts/', post_list, name='post_list'),  # List of posts
    path('posts/create/', post_create, name='post_create'),  # Create post
    path('posts/<int:pk>/', post_detail, name='post_detail'),  # Post detail
    path('logout/', logout_view, name='logout'),  # Logout
]
