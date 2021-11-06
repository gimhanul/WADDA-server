from django.contrib import admin
from .models import Sight, SightImages

class PhotoInline(admin.TabularInline):
    model = SightImages

class SightAdmin(admin.ModelAdmin):
    list_display = ('name', 'tags', 'address', 'tel', 'time', 'closed', 'description')
    inlines = [PhotoInline, ]

    fieldsets = (
        (None, {'fields': ('name',)}),
        ('tags', {'fields': ('tags',)}),
        ('Info', {'fields': ('address', 'tel', 'time', 'closed', 'description')}),
    )
    search_fields = ['name']

admin.site.register(Sight, SightAdmin)
