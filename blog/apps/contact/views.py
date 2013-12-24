from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from contact.forms import ContactForm


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form.send()
		return HttpResponseRedirect(reverse('contact'))

	return render_to_response('contact/contact.html', 
							{'form':form}, context_instance=RequestContext(request))
