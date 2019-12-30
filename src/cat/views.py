from django.shortcuts import render


def home(request):
    return render(request, 'cat/index.html', {'title:': 'Category'})
