from django.urls import path
from . import views
from .views import ultima_publicacion, detalle_publicacion

app_name = 'myblog'

urlpatterns = [
    path('', views.index, name='post_list'),
    path('ultima_publicacion/', ultima_publicacion, name='ultima_publicacion'),
     path('ultima_publicacion/', ultima_publicacion, name='ultima_publicacion'),
    path('detalle_publicacion/<int:publicacion_id>/', detalle_publicacion, name='detalle_publicacion'),
    #path('category/<int:category_id>/', category_posts, name='category_posts'),
   # path('post/<int:post_id>/', post_detail, name='post_detail'),
   # path('tag/<int:tag_id>/', tag_posts, name='tag_posts'),
]