from django.shortcuts import render_to_response
from django.template import RequestContext

from hitthescene.event.models import Event

def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def eventlist(request):
    events = Event.objects.all()
    return render_to_response('eventlist.html', {'events': events}, context_instance=RequestContext(request))
