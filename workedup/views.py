from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from .models import Recipe, Favorite


# Create your views here.
# @login_required(login_url='login')
def index(request):
    return render(request, 'workedup/index.html')


def about(request):
    return render(request, 'workedup/info.html')


@login_required(login_url='login')
def create_recipe(request):
    form = RecipeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('browse')

    context = {'form': form}
    return render(request, 'workedup/create_recipe.html', context)


@login_required(login_url='login')
def browse(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'workedup/browse.html', context)


@login_required(login_url='login')
def view_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    favorites = Favorite.objects.all()
    context = {'recipe': recipe, 'favorites': favorites}
    return render(request, 'workedup/view_recipe.html', context)


@login_required(login_url='login')
def manage_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if recipe.user == request.user or request.user.is_superuser:
        form = RecipeForm(request.POST or None, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('browse')
        return render(request, 'workedup/manage_recipe.html', {'form': form})
    else:
        return redirect('browse')


@login_required(login_url='login')
def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if recipe.user == request.user or request.user.is_superuser:
        recipe.delete()
        return redirect('browse')
    return redirect('browse')


@login_required(login_url='login')
def toggle_favorite(request, id):
    recipe = Recipe.objects.get(id=id)
    favorites = Favorite.objects.all()
    for favorite in favorites:
        if favorite.user == request.user and favorite.recipe == recipe:
            favorite.delete()
            return redirect('view_recipe', id)
    Favorite.objects.create(recipe=recipe, user=request.user)
    return redirect(view_recipe, id)


@login_required(login_url='login')
def favorites(request):
    favorite = Favorite.objects.all()
    context = {'favorites': favorite}
    return render(request, 'workedup/favorites.html', context)