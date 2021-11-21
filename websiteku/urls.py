from django.contrib import admin
from django.urls import path, include

from . import views
from about import views as viewsAbout

urlpatterns = [
    path('about/', include('about.urls')),
    path('recent/', viewsAbout.recent),
    path('history/', viewsAbout.history),
    path('blog/', views.blog),
    path('', views.index),
    path('admin/', admin.site.urls),
]
