from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from posts.models import Category, Post
from comments.forms import CommentForm
from datetime import datetime 


def list(request):
	posts = Post.objects.all()
	return render_to_response('posts/post_list.html',
			{'posts': posts}, context_instance=RequestContext(request))

def detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	posts_related = post.tags.similar_objects()
	comments = post.comments.filter(is_public=True).order_by('-submit_date')
	#comment

	form = CommentForm(request.POST or None)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.submit_date = datetime.now()
		comment.user_name = form.cleaned_data['user_name']
		comment.user_email = form.cleaned_data['user_email']
		comment.site = Site.objects.get_current()
		comment.ip_address = request.META.get("REMOTE_ADDR", None)
		comment.content_type = ContentType.objects.get_for_model(post)
		comment.object_pk = post.id
		comment.save()
		return HttpResponseRedirect(reverse('post_detail',args=(post.slug,)))
    
	return render_to_response('posts/post_detail.html',
			{'post': post, 'posts_related': posts_related, 'form': form, 'comments': comments}, context_instance=RequestContext(request))