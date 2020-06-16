from django.shortcuts import render
from django.http import HttpResponse


class Finch:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age


finches = [
    Finch('Desmond', 'house finch', 'foul little demon', 666),
    Finch('Snorlax', 'european goldfinch', 'sleeps all day', 0),
    Finch('Odin', 'common chaffinch', 'has one eye and a mean stare', 12)
]


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})
