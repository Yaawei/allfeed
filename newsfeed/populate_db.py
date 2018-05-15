from .models import NewsPiece
from dateutil.parser import parse as date_parse
from dateutil.tz import *


def populate_from_scraper(scraped):
    for piece in scraped:
        pub_date = date_parse(get_string(piece.get('Publish Date')))
        author = get_string(piece.get('Author'))
        title = get_string(piece.get('Title'))
        description = get_string(piece.get('Description'))
        link = get_string(piece.get('Link'))
        rss_id = piece.get('Rss_id')
#todo naprawic timezony
        NewsPiece.objects.get_or_create(
            title=title,
            url=link,
            author=author,
            publish_date=pub_date,
            description=description,
            rss_source_id= rss_id
        )


def get_string(value):
    try:
        return value.get_text()
    except AttributeError:
        return value
