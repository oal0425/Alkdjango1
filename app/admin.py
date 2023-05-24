from django.contrib import admin
from .models import Person, Tweet


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'birth', 'is_active')


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'created_at', 'modified_at')