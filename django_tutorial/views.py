from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def redirect(request):
  return HttpResponseRedirect(reverse('polls:index'))
