from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from .forms import *
from .filters import EventFilter

# Create your views here.
class eventView(View):
    template_name = "user/event.html"

    def get(self, request):
        eventList = Event.objects.all()

        myFilter = EventFilter(request.GET, queryset=eventList)
        eventList = myFilter.qs

        context = {'eventList':eventList, 'myFilter':myFilter}

        return render(request, self.template_name, context)

class loginView(View):
    template_name = "user/login.html"

    def get(self, request):
        return render(request, self.template_name)

class registerView(View):
    template_name = "user/register.html"

    def get(self, request):
        return render(request, self.template_name)

class organizedEventsView(View):
    template_name = "user/organizedEvents.html"

    def get(self, request):
        return render(request, self.template_name)

class createEventView(View):
    template_name = "user/createEvent.html"

    def get(self, request):
        return render(request, self.template_name)

class requestJoinView(View):
    template_name = "user/requestJoin.html"

    def get(self, request):
        return render(request, self.template_name)

class joinListView(View):
    template_name = "user/joinList.html"

    def get(self, request):
        return render(request, self.template_name)

class updateEventView(View):
    template_name = "user/updateEvent.html"

    def get(self, request):
        return render(request, self.template_name)

class viewDetailsView(View):
    template_name = "user/viewDetails.html"

    def get(self, request):
        return render(request, self.template_name)

class roleRequestView(View):
    template_name = "user/roleRequest.html"

    def get(self, request):
        return render(request, self.template_name)

     