import django.conf.urls
from . import views

urlpatterns = [
    django.conf.urls.url('', views.post_list, name='post_list')
]
