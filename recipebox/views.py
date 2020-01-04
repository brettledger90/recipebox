from django.shortcuts import render
from recipebox.models import Recipe, Author
from recipebox.forms import RecipeAdd, AuthorAdd
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def index(request):
    html = "index.html"
    recipe= Recipe.objects.all()
    return render(request, html, {'data':recipe})

def detail(request, id):
    html= "detail.html"
    recipes = Recipe.objects.filter(id=id)
    return render(request, html, {'recipes':recipes})

def authorview(request, id):
    html = "authorview.html"
    author = Author.objects.filter(id=id)
    author_recipe = Recipe.objects.filter(author=id)
    return render(request,html, {'author' : author , 'author_recipe' : author_recipe})


@login_required
def recipe_add(request):
    html = "recipe_add.html"
    form = None
    if request.method == "POST":
        form = RecipeAdd(request.POST)

        if form.is_valid():
            data= form.cleaned_data
            Recipe.objects.create(
                title = data['title'],
                author = data['author'],
                description = data['description'],
                instructions = data['instructions'],
                timerequired = data['timerequired']
            )
            return render(request, 'completed.html')
        
    else:
        form = RecipeAdd()
    return render(request,html, {"form" : form})

@staff_member_required
def author_add(request):
    html = 'author_add.html'
    form = None

    if request.method == "POST":
        form = AuthorAdd(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Author.objects.create(
                name = data['name']
            )
        return render(request, 'completed.html')

    else:
        form = AuthorAdd()
    return render(request, html, {"form" : form})

        





