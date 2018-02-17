from django.conf.urls import url

from . import views

app_name = 'people'
urlpatterns = [
    # ex: /people/
    url(r'^$', views.index, name='index'),
    # ex: /people/jasper/
    url(r'^(?P<name>[a-z]+)/$', views.detail, name='detail')
]
