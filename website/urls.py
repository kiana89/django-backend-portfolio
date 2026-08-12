from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('blog/post/', single_post, name='single_post'),
]