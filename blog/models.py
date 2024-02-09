from django.db import models
from django.contrib.auth import get_user_model
from blog.managers import PostDraftMangers


User = get_user_model()


class Post(models.Model):

    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    liked_post = models.ManyToManyField(User, related_name='liked', blank=True)
    saved_post = models.ManyToManyField(User, related_name='saved', blank=True)

    object = models.Manager()
    draft = PostDraftMangers()

    class Meta:
        ordering = ('-created', )

    @property
    def number_of_liked(self):
        return self.liked_post.count()

    @property
    def number_of_comments(self):
        return self.comments.count()

    def __str__(self):
        return self.name


class Entry(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='entries')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')

    headline = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='files/entries/', blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.name


class Comments(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.name
