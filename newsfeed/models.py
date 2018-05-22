from django.db import models
from django.contrib.auth.models import User
import urllib.parse


class RssUrl(models.Model):
    base_address = models.CharField(max_length=128)
    tail_address = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    parser_template = models.ForeignKey('ParserSets', on_delete=models.CASCADE, default=1)
    user_choices = models.ManyToManyField(User, through='UserFeedChoices')

    def __repr__(self):
        return urllib.parse.urljoin(self.base_address, self.tail_address)


class NewsPiece(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    description = models.TextField(max_length=20000)
    url = models.CharField(max_length=255)
    author = models.CharField(max_length=100, null=True)
    rss_source = models.ForeignKey(
        'RssUrl',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        unique_together = (
            "title",
            "publish_date",
            "description",
            "url",
            "author",
            "rss_source"
        )

    def __repr__(self):
        return '%s (%s)' % (type(self), self.pk)

    def site_filtered_queryset(*args):
        listargs = [num for arg in args for num in arg]
        return NewsPiece.objects.filter(rss_source__pk__in=listargs).order_by('-publish_date')


class UserFeedChoices(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rss_url = models.ForeignKey(RssUrl, on_delete=models.CASCADE)

    def __repr__(self):
        return '%s (%s)' % (type(self), self.pk)


class ParserSets(models.Model):
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=20)
    publish_date = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    item = models.CharField(max_length=20)

    def __repr__(self):
        return '%s (%s)' % (type(self), self.pk)
