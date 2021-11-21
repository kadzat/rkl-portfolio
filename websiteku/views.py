from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'judul': 'latihan django',
        'subjudul': 'INI ADALAH HOME',
        'editor': 'rendi',
        'banner': 'img/banner_home.png',
        'nav': [
            ['/', 'Home'],
            ['/blog/', 'Blog'],
            ['/about/', 'About'],
            ['/recent/', 'Recent'],
            ['/history', 'History'],
        ]
    }
    return render(request, 'index.html', context)


def blog(request):
    context = {
        'judul': 'latihan django',
        'subjudul': 'INI ADALAH HALAMAN BLOG',
        'editor': 'reki',
        'banner': 'img/banner_blog.png',
        'nav': [
            ['/', 'Home'],
            ['/blog/', 'Blog'],
            ['/about/', 'About'],
            ['/recent/', 'Recent'],
            ['/history', 'History'],
        ]
    }
    return render(request, 'index.html', context)
