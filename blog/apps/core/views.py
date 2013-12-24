from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from posts.models import Category, Post
from core.forms import PostSearchForm

def index(request):
	posts_highlight = Post.objects.filter(is_highlight=True)
	posts = Post.objects.exclude(is_highlight=True)	
	return render_to_response('index.html',{
			'posts_highlight': posts_highlight,
			'posts': posts},context_instance=RequestContext(request))

def search(request):
	form = PostSearchForm(request.GET)
	posts = form.search()	
	print posts
	return render_to_response('search/search_result.html', {'posts': posts}, context_instance=RequestContext(request))