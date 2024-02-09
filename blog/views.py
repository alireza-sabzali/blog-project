from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


from blog.models import Post, Comments, Entry
from blog.serializers import PostSerializer, CommentSerializer,\
    EntrySerializer, PostCommentSerializer


class PostListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    queryset = Post.object.all()
    serializer_class = PostSerializer

    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields  = ['status']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Post.object.all()
    serializer_class = PostSerializer


class PostCommentView(RetrieveAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    queryset = Post.object.all()
    serializer_class = PostCommentSerializer


class CommentCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )

    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class EntryCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )

    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
