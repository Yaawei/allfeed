from django.db import models
from django.contrib.auth.models import User
from newsfeed.models import NewsPiece


class LikedEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_entry = models.ForeignKey(NewsPiece, on_delete=models.CASCADE)

    def __repr__(self):
        return '%s (%s)' % (type(self), self.pk)

