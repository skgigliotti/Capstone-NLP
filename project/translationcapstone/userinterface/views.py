from django.http import HttpResponse
from django.shortcuts import render
from .forms import TextForm
from .models import Question
from .models import Post
from .markov import predictions

def results(request, question_id):
    response = "Here are the questions %s"
    return HttpResponse(response % question_id)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.all()

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'index.html', context)

def text_view(request):
    if request.method == "POST":

        texts = [request.POST.get('option1'),request.POST.get('option2')]
        #Question.objects.create(question_text=text)
        probabilities = predictions.train(texts)
        
    context = {}
    return render(request, "enter_options.html",context)
