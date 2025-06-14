from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import Lead, Agent

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )
        


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {
            "username": UsernameField,
        }

class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        print(kwargs)
        super().__init__(*args, **kwargs)

        # Filter to only show leads under the user's organization
        agents = Agent.objects.filter(organization=request.user.userprofile)
        self.fields["agent"].queryset = agents
        
