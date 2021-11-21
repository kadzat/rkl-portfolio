from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'judul': 'latihan django',
        'subjudul': 'INI ADALAH HALAMAN ABOUT',
        'editor': 'ronaldo',
        'banner': 'about/img/banner_about.png',
        'nav': [
            ['/', 'Home'],
            ['/blog/', 'Blog'],
            ['/about/', 'About'],
            ['/recent/', 'Recent'],
            ['/history', 'History'],
        ]

    }
    return render(request, 'index.html', context)


def recent(request):
    context = {
        'judul': 'latihan django',
        'subjudul': 'INI ADALAH HALAMAN RECENT',
        'editor': 'ronaldo wati',
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


def history(request):
    context = {
        'judul': 'latihan django',
        'subjudul': 'INI ADALAH HALAMAN HISTORY',
        'editor': 'ASEP BALON',
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
