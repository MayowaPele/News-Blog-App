from Posts.models import Post
from django.urls import path
from Posts import views
from Posts.views import PostAPIView

urlpatterns = [
    path('index/', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('post/', views.post, name='post'),
    path('postview/', PostAPIView.as_view())
]
