from django.http import HttpResponse
from django.shortcuts import render
from .forms import TextForm
from .models import Question
from .models import Post
from .markov import predictions
from .sentiment import processingsingular

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

def markov_view(request):
    if request.method == "POST":
        #get the different information from the form
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        original = request.POST.get('original')
        target = request.POST.get('target')

        #check for what has actually been filled in
        if ((option1 != '') and (option2 != '')):
            texts = [option1,option2]
            probabilities = predictions.train(texts)
            print(probabilities)
        if (( original != '') and ( target != '' )):
            texts = [original,target]
            print(texts)
            processingsingular.analyze(texts)
            #Translation.objects.create(original=original,target=target)
    context = {}
    return render(request, "enter_options.html",context)
