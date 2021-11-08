from django.shortcuts import render
from .models import Sight

def q(request, question_id):
    return

def sight(request, sight_id):
    sight = Sight.objects.get(id = sight_id)
    print(sight.tags)

    context = {
        's': sight
    }
    return render(request, 'sight.html', context)
