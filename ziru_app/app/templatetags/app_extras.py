from django import template
import markdown2
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """Converts markdown text to HTML"""
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
