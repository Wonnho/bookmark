from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Question, Choice

# from django.
# Create your views here.

def index(request):
    question_list=Question.objects.order_by('-pub_date')[:5]
    
   # output=','.join([q.question_text for q in question_list])
   # return HttpResponse(output)

    template=loader.get_template('polls/index.html')
    context={ 'question_list':question_list,}
    return HttpResponse(template.render(context,request))

def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExits:
        raise Http404("Question does not exist")
   #return HttpResponse("You are looking at question $s." % question_id)
    return render(request,'polls/detail.html',{'question':question}) 


def results(request,question_id):
   
    #response="You are looking at question %s."
    question=get_object_or_404(question,pk=question_id)
    #return HttpResponse(response % question_id)
    return render(request,'polls/results.html',{'question':question})

    
def vote(request,question_id):
    question=get_object_or_404(question,pk=question_id)
    try:
        selected_choice=qeustion.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,
        'error_message':"You didn't select a choice",})
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResposeRedirect(reverse('polls:results',args=(question.id,)))
    #return HttpResponse("You are looking at question $s." % question_id)