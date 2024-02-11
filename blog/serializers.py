from rest_framework import serializers
from blog.models import Post, Entry, Comments
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', )


class EntrySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Entry
        fields = ('id', 'post', 'author', 'headline', 'image', 'description', 'created')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comments
        fields = ('id', 'post', 'author', 'created', 'description')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    entries = EntrySerializer(many=True, read_only=True)
    liked_post = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'name', 'created', 'entries', 'liked_post', 'number_of_comments')


class PostCommentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('comments', )
