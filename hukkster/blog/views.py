from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from blog.models import *

def main(request):
	#front page of blog
	posts = Post.objects.all().order_by("-created")
	paginator = Paginator(posts, 2)

	try: 
		page = int(request.GET.get("page", '1'))
	except ValueError:
		page = 1

	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)

	return render_to_response("list.html", dict(posts=posts, user=request.user))

def post(request):
	return render_to_response("Yo")