from bs4 import BeautifulSoup
import urllib.parse
import requests
from .models import RssUrl, ParserSet
from .populate_db import populate_from_scraper


HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/39.0.2171.95 '
                         'Safari/537.36'}


def _get_rss_contents(address, rss_id, template_id):
    response = requests.get(address, headers=HEADERS)
    return _parse_rss_contents(response.text, rss_id, template_id)


def _parse_rss_contents(rss_feed, rss_id, template_id):
    template = ParserSet.objects.get(pk=template_id)
    soup = BeautifulSoup(rss_feed, "xml")
    items = soup.find_all(template.item)
    results = [{
            'Title': item.find(template.title),
            'Link': item.find(template.link),
            'Publish Date': item.find(template.publish_date),
            'Author': item.find(template.author),
            'Description': item.find(template.description),
            'Rss_id': rss_id
        } for item in items]
    return results


def scrape():
    result = []
    for entry in RssUrl.objects.all():
        result.extend(_get_rss_contents(
            address=urllib.parse.urljoin(
                entry.base_address,
                entry.tail_address
            ),
            rss_id=entry.id,
            template_id=entry.parser_template_id
        ))
    populate_from_scraper(result)
