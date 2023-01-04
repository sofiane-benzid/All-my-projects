from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
import random

import markdown


from . import util

class Search(forms.Form):
    q = forms.CharField(label='')
class Title(forms.Form):
    title = forms.CharField(label='Title')
    text = forms.CharField(widget=forms.Textarea)
class Text(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

def markdown_to_html(title):
    content = util.get_entry(title)
    if content == None:
        return None
    md = markdown.Markdown()
    text = md.convert(content)
    return text


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form" : Search()   
    })

def titles(request, title):
    text = markdown_to_html(title)
    return render(request, "encyclopedia/title.html",{
    "title" : text,
    "titre" : title})
    

def search(request):
    sl = []
    form = Search(request.GET)
    if form.is_valid():
        q = form.cleaned_data["q"]
        entry = util.list_entries()
        if q in entry:
            for i in range(len(entry)):
                if q == entry[i]:
                    return render(request, "encyclopedia/title.html",
                        {
                            "title" : markdown_to_html(q)
                        })
        

        for i in range(len(entry)):
            if q in entry[i]:
                sl.append(entry[i])
        return render(request, "encyclopedia/index.html", {
            "entries": sl,
        })
        
    else:
        return render(request, "encyclopedia/index.html",{
            "form": form})

def create(request):
    if request.method == "POST":
        form2 = Title(request.POST)
        if form2.is_valid():
            title = form2.cleaned_data["title"]
            text = form2.cleaned_data["text"]
            if title in util.list_entries():
                return HttpResponse("Error: page with given title already exists.")
            util.save_entry(title, text)
        return HttpResponseRedirect(f"/wiki/{title}")
    else:
        return render(request, "encyclopedia/create.html",{
            "form2" : Title()
        })
def rndm(request):
    list = util.list_entries()
    i = random.randint(0, len(list)-1)
    return HttpResponseRedirect(f"/wiki/{list[i]}")

def edit(request):
    title = request.POST['title']
    text = request.POST['text']
    form = Text(initial={'text': text})
    return render(request, "encyclopedia/edit.html", {
        "title" : title,
        "text" : text,
        "form3" : form
    })

def save(request):
    title = request.POST['title']
    form = Text(request.POST)
    if form.is_valid():
        text = form.cleaned_data["text"]
    util.save_entry(title, text)
    return HttpResponseRedirect(f"/wiki/{title}")



    



        