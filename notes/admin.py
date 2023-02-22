from django.contrib import admin

from .models import Note


@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
    )
