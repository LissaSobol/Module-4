from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm

def index(request):
    advertisements = Advertisement.objects.all()
    context = {"advertisements" : advertisements}
    return render(request,"index.html", context)

def top_sellers(request):
    return render(request, "top-sellers.html")

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            url = reverse('main-page')
            return redirect(url)

    
    else: 
        form = AdvertisementForm()
    context = {"form" : form}
    return render(request, "advertisement-post.html", context)

def advertisement(request):
    return render(request, "advertisement.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def profile(request):
    return render(request, "profile.html")
# Create your views here.
