from .models import NewsPiece
from dateutil.parser import parse as date_parse
from dateutil.tz import gettz
from .readability import get_string

tzinfos = {"EDT": gettz('SA Western Standard Time')}


def populate_from_scraper(scraped):
    for piece in scraped:
        NewsPiece.objects.get_or_create(
            title=get_string(piece.get('Title')),
            url=get_string(piece.get('Link')),
            author=get_string(piece.get('Author')),
            publish_date=date_parse(
                get_string(piece.get('Publish Date')),
                tzinfos=tzinfos
            ),
            description=get_string(piece.get('Description')),
            rss_source_id=piece.get('Rss_id')
        )


