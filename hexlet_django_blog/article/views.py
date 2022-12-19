from django.shortcuts import render


def index(request):
    return render(request, 'article.html', context={
        'name': 'Articles',
    })
