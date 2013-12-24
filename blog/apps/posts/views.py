from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from posts.models import Category, Post

def list(request):
	posts = Post.objects.all()
	return render_to_response('posts/post_list.html',
			{'posts': posts}, context_instance=RequestContext(request))

def detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render_to_response('posts/post_detail.html',
			{'post': post}, context_instance=RequestContext(request))