from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/index.html")

# contact view

def contact(request):
    return render(request, "core/contact.html")