from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^profile/(\d+)',views.profile,name = "profile"),
    url(r'^create/post',views.new_post, name = "new-post"),
    url(r'^follow/(\d+)', views.follow, name = "follow"),
    url(r'^likes/(\d+)' ,views.likes , name = "likes"),
    url(r'^post/(\d+)',views.post,name = "post"),
    url(r'^create/comment/$', views.comment, name="comment" ),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)