from django.urls import path
from .views import BlogListView, BlogDetailView, CreatePostView, \
    ReservedDetailView, AboutPostView, TeamPostView, NewsPostView, BlogPostView, ContactPostView

urlpatterns = [
    path('post/', CreatePostView.as_view(), name='add_post'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/', ReservedDetailView.as_view(), name='post_reserved'),
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutPostView.as_view(), name='about'),
    path('team/', TeamPostView.as_view(), name='team'),
    path('news/', NewsPostView.as_view(), name="news"),
    path('blog/', BlogPostView.as_view(), name='blog'),
    path('contact/', ContactPostView.as_view(), name='contact')

]

