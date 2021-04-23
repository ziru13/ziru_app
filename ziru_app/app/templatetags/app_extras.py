from django import template

from ..models import Post


register = template.Library()

# @register.simple_tag
# def newest_post():
#     """ Gets the most recent post that was added to the library. """
#     posts = Post.objects.all().order_by('-created_at')[:5]
#     return posts

