from django import template

register = template.Library()

@register.filter(name='shorten')
def shorten(content):
	#will show up to the first 500 characters of the post content
	return content[:500]