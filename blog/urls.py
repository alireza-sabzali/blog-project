from django.urls import path
from blog.views import PostListCreateView, PostRetrieveUpdateDeleteView,\
    CommentCreateView, PostCommentView, EntryCreateView

app_name = 'blog'

urlpatterns = [
    path('post/', PostListCreateView.as_view()),
    path('post/<int:pk>/', PostRetrieveUpdateDeleteView.as_view()),
    path('post/comments/<int:pk>/', PostCommentView.as_view()),
    path('post/comment/create/', CommentCreateView.as_view()),
    path('post/entry/create/', EntryCreateView.as_view()),
]
