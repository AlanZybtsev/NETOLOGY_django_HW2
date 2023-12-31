from django.shortcuts import render, reverse

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

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def home_view(request):
    template_name = 'calculator/home.html'
    recipes = {k: reverse(k) for k, v in DATA.items()}
    context = {
        'recipes': recipes
    }
    return render(request, template_name, context)


def omlet(request):
    template_name = 'calculator/omlet.html'
    servings = request.GET.get('servings', 1)
    ingredients = DATA.get('omlet', {}).copy()
    for ingredient in ingredients:
        ingredients[ingredient] = round((ingredients[ingredient] * int(servings)), 2)
    # print(ingredients)
    context = {
        'ingredients': ingredients
    }
    # print(request.GET)
    return render(request, template_name, context)


def pasta(request):
    template_name = 'calculator/pasta.html'
    servings = request.GET.get('servings', 1)
    ingredients = DATA.get('pasta', {}).copy()
    for ingredient in ingredients:
        ingredients[ingredient] = round((ingredients[ingredient] * int(servings)), 2)
    # print(ingredients)
    context = {
        'ingredients': ingredients
    }
    # print(request.GET)
    return render(request, template_name, context)

def buter(request):
    template_name = 'calculator/buter.html'
    servings = request.GET.get('servings', 1)
    ingredients = DATA.get('buter', {}).copy()
    for ingredient in ingredients:
        ingredients[ingredient] = round((ingredients[ingredient] * int(servings)), 2)
    # print(ingredients)
    context = {
        'ingredients': ingredients
    }
    # print(request.GET)
    return render(request, template_name, context)
