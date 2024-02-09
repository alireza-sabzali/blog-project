from django.db import models


class PostDraftMangers(models.Manager):

    def get_queryset(self):
        return super(PostDraftMangers, self).get_queryset().filter(status='draft')
