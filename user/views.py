from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import UserCreationForm, AuthenticationForm
from .models import User

def index(request):
    return render(request, 'index.html')



#join
def join(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'join.html', context)



#login
def userlogin(request):
    context = {}
    user = request.user
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


#setting
def setting(request):
    if request.method == 'POST':
        setting = request.POST.get('setting')
        if setting == 'logout':
            logout(request)
            return redirect('/')
        if setting == 'withdraw':
            user = User.objects.get(id=request.user.id)
            user.delete()
            return redirect('/')
        
    return render(request, 'setting.html')