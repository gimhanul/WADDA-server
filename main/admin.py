from django.contrib import admin
from .models import Sight


class SightAdmin(admin.ModelAdmin):
    list_display = ('name', 'tags', 'address', 'tel', 'time', 'closed', 'description', 'image')

    fieldsets = (
        (None, {'fields': ('name',)}),
        ('tags', {'fields': ('tags',)}),
        ('Info', {'fields': ('address', 'tel', 'time', 'closed', 'description', 'image')}),
    )
    search_fields = ['name']

admin.site.register(Sight, SightAdmin)
