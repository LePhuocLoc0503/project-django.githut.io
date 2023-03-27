from django.shortcuts import render
from .models import Question , Questions
from django.http import HttpResponse
# Create your views here.
def index(request):
    myname ="abcabcabc"
    abc =["abcb","masi","asdsa"]
    context = { "name": myname ,"text":abc }
    return render(request, "polls/index.html", context )

def viewlist(request):
    list_question= Question.objects.all()
    context = {"dsquest": list_question}
    return render(request,"polls/question_list.html",context)

def detail(request,questions_id):
    ids = Questions.objects.get(pk=questions_id)
    return render(request, "polls/detail.html", {"a": ids})



