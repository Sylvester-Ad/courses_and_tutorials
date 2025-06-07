from django.forms import ModelForm
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganizerAndLoginRequiredMixin



class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    """
    View to list all agents.
    Requires the user to be logged in.
    """
    model = Agent
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return self.model.objects.filter(organization=request_user_organization)
    

class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    """
    View to create a new agent.
    Requires the user to be logged in.
    """
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agents:agent_list")
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    """
    View to display details of a specific agent.
    Requires the user to be logged in.
    """
    model = Agent
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return self.model.objects.filter(organization=request_user_organization)

class AgentUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    """
    View to update an existing agent.
    Requires the user to be logged in.
    """
    model = Agent
    template_name = "agents/agent_update.html"
    context_object_name = "agent"
    form_class = AgentModelForm

    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return self.model.objects.filter(organization=request_user_organization)

    def get_success_url(self):
        return reverse("agents:agent_list")

    
class AgentDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    """
    View to delete an existing agent.
    Requires the user to be logged in.
    """
    model = Agent
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"

    def get_queryset(self):
        request_user_organization = self.request.user.userprofile
        return self.model.objects.filter(organization=request_user_organization)
    
    def get_success_url(self):
        return reverse("agents:agent_list")
    
