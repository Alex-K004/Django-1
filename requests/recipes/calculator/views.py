from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def omlet(request):
    servings = int(request.GET.get('servings', 1))
    base_recipe =  {
            'яйца, шт': '2',
            'молоко, л': '0.1',
            'соль, ч.л.': '0.5',
        }
    recipe = {}
    for ingredient, amount in base_recipe.items():
        recipe[ingredient] = round(float(amount) * servings, 2)
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = int(request.GET.get('servings', 1))
    base_recipe =  {
             'макароны, г': '0.3',
             'сыр, г': '0.05',
        }
    recipe = {}
    for ingredient, amount in base_recipe.items():
        recipe[ingredient] = round(float(amount) * servings, 2)
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)

def buter(request):
    servings = int(request.GET.get('servings', 1))
    base_recipe =  {
        'хлеб, ломтик': '1',
        'колбаса, ломтик': '1',
        'сыр, ломтик': '1',
        'помидор, ломтик': '1',
        }
    recipe = {}
    for ingredient, amount in base_recipe.items():
        recipe[ingredient] = round(float(amount) * servings, 2)
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)

