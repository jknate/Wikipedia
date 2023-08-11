from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from markdown2 import Markdown
from . import util
import random

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    entry = forms.CharField(label="Entry", widget = forms.Textarea())

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def convert(mdtext):
    markdowner = Markdown()
    return markdowner.convert(mdtext)
def description(request, name):
    if util.get_entry(name) == None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page Does Not Exist"
        })
    return render(request, "encyclopedia/description.html", {
        "text": convert(util.get_entry(name)),
        "name": name
    })
def search(request):
    if request.method == "POST":
        list = util.list_entries()
        query = request.POST['q']
        if util.get_entry(query) == None:
            results = []
            for entry in list:
                if query in entry:
                    results.append(entry)
            if len(results) == 0:
                return render(request, "encyclopedia/search.html", {
                "message": "Sorry, there are no corresponding pages"
            })
            return render(request, "encyclopedia/search.html", {
                "results": results
            })
        
        return render(request, "encyclopedia/description.html", {
            "text": convert(util.get_entry(query)),
            "name": query
        })
def newpage(request):

    if request.method == "POST":
        form = NewPageForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            entry = form.cleaned_data["entry"]
            if util.get_entry(title) != None:
                return render(request, "encyclopedia/error.html", {
                    "message": "Title Already In Use"
                })
            util.save_entry(title, entry)
            return render(request, "encyclopedia/description.html", {
            "text": convert(entry),
            "name": title
            })
        else:
            return render(request, "encyclopedia/newpage.html", {
                "form": form 
            })

    return render(request, "encyclopedia/newpage.html", {
        "form": NewPageForm()
    })
def edit(request, name):
    if util.get_entry(name) == None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page Does Not Exist"
        })

    return render(request, "encyclopedia/edit.html", {
        "name": name,
        "text": util.get_entry(name)
    })
def save_edit(request, name):
    if request.method == "POST":
        new_entry = request.POST['editbox'] 
    
        util.save_entry(name, new_entry)
        return render(request, "encyclopedia/description.html", {
            "name": name,
            "text": convert(util.get_entry(name))
        })
def random_page(request):
    name = random.choice(util.list_entries())
    return render(request, "encyclopedia/description.html", {
        "name": name,
        "text": convert(util.get_entry(name))
    })