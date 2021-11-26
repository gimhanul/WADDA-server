from django.contrib import admin
from .models import Choice, Sight, Question

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', )
    inlines = [ChoiceInline]

    fieldsets = [
        (None, {'fields': ['question']}),
    ]
    search_fields = ['question']

class SightAdmin(admin.ModelAdmin):
    list_display = ('name', 'tags', 'address', 'tel', 'time', 'closed', 'description', 'image')

    fieldsets = (
        (None, {'fields': ('name',)}),
        ('tags', {'fields': ('tags',)}),
        ('Info', {'fields': ('address', 'tel', 'time', 'closed', 'description', 'image')}),
    )
    search_fields = ['name']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Sight, SightAdmin)