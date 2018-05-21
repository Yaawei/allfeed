from django import template
from ..models import NewsPiece

register = template.Library()


@register.simple_tag
def filtered_querysets(*args):
    return NewsPiece.site_filtered_queryset(args)