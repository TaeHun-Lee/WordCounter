from django.shortcuts import render
import re

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    var_fulltext = request.GET['fulltext']
    var_splitted = re.findall(r"[\w']+", var_fulltext)
    dic_words = {}
    for i in var_splitted :
        if i in dic_words :
            dic_words[i] += 1
        else :
            dic_words[i] = 1
    return render(request, 'result.html', {"full" : var_fulltext, "total_len" : len(var_splitted),
    "pairs" : dic_words.items() })