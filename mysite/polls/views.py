from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.template import loader
from .models import Question
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  #must note it's -pub_date!!!
    template = loader.get_template('polls/index.html')                 #remember the direction!! 
    context = {
        'latest_question_list': latest_question_list,
    }    
    #return HttpResponse(template.render(context, request))               #use tmplate.render !!! 
    
    return render(request,'polls/index.html',context)                   #shortcut
    

# Create your views here.
def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    #question = get_object_or_404(Question,pk = question_id)               #just short cut to check if the Question exist or not
    return render(request,'polls/detail.html',{'question':question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)