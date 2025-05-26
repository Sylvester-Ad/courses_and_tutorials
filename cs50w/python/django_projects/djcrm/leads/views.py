from django.shortcuts import render
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# My views.


def index(request):
    leads = Lead.objects.all()

    return render(request, "leads/index.html", {
        "leads": leads,
    })

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)


    return render(request, "leads/lead_detail.html", {
        "lead": lead,
    })

def lead_create(request):
    form = LeadModelForm()

    if request.method == "POST":
        form = LeadModelForm(request.POST)

        # Validate form
        if form.is_valid():
            form.save()
            print("Lead created successfully in database")
            return HttpResponseRedirect(reverse("leads:index"))
    return render(request, "leads/lead_create.html", {
        "form": form
    })



# def lead_create(request):
#     form = LeadForm()

#     if request.method == "POST":
#         form = LeadForm(request.POST)

#         # Validate form
#         if form.is_valid():
#             print("The form is valid")
#             print(form.cleaned_data)
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             agent = Agent.objects.first()

#             # Create the new lead in the database
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             print("Lead created successfully in database")
#             return HttpResponseRedirect(reverse("leads:index"))
#     return render(request, "leads/lead_create.html", {
#         "form": form
#     })