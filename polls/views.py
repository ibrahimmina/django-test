from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Question
from .forms import QuestionForm

def ques(request):  
    if request.method == "POST":  
        form = QuestionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = QuestionForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    questions = Question.objects.all()  
    return render(request,"show.html",{'questions':questions})  
def edit(request, id):  
    question = Question.objects.get(id=id)  
    return render(request,'edit.html', {'question':question})  
def update(request, id):  
    question = Question.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = question)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'question': question})  
def destroy(request, id):  
    question = Question.objects.get(id=id)  
    question.delete()  
    return redirect("/show")  