from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list = ('name', 'genre', 'starring')

    admin.site.register(Movie)