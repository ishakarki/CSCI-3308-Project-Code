from django.conf.urls import url 
from . import views 
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url

app_name = 'music'

urlpatterns = [
    #/music/
    url(r'^$', views.home, name = 'home'),

	#/music/index
    url(r'^index$', views.IndexView.as_view(), name = 'index'),

    #/music/queue
    url(r'^queue$', views.QueueView.as_view(), name = 'queue'),

    url(r'^register/$', views.UserFormView.as_view(), name = 'register'),

    #/music/<album id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name= 'detail'),

    #music/album/add/
    url(r'album/add/$',views.AlbumCreate.as_view(), name = 'album-add'),

    #music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name = 'album-update'),

    #music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(), name = 'album-delete'),

    #/music/<album id>/addqueue/
    url(r'^(?P<album_id>[0-9]+)/addqueue/$', views.addqueue, name= 'addqueue'),



]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)