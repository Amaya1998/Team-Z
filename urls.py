from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ViewPost, name='posts'),
    path('form/', CreatePost, name='form'),
    path('register/', Register, name='register'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)