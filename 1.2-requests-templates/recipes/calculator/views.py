from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'soup': {
        'вода, л': 0.3,
        'мясо, кг': 0.1,
        'картофель, кг': 0.05,
        'грибы, кг': 0.03,
    },
}


def dish(request, dish):
    servings = int(request.GET.get('servings', 1))
    ingredients, dish_name = dict(), ''
    if dish in DATA:
        dish_name = dish
        ingredients = {key: (value * servings) for key, value in DATA[dish].items()}
    context = {'recipe': ingredients,
               'dish_name': dish_name}
    return render(request, 'calculator/index.html', context)


def home_view(request):
    pages = dict()
    for dish in DATA:
        pages[f'{dish}'] = f'/{dish}/'
    context = {
        'pages': pages
    }
    return render(request, 'calculator/team.html', context)
