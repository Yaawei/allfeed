from __future__ import absolute_import
from celery import task
from .parser import scrape


@task
def run_scraper():
    scrape()
