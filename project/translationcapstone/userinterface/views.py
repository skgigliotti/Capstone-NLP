from django.http import HttpResponse
from django.shortcuts import render
from .forms import TextForm

from .models import Post

def index(request):
    return HttpResponse("Hello, world.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def box_view(request):
    form = TextForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TextForm()
    context = {
        'form': form
    }
    return render(request, "enter_info.html", context)
