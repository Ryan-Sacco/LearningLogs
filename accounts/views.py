from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register A New "User"""
    if request.method != 'POST':
            form = UserCreationForm()
    form = UserCreationForm(data=request.POST)
    
    if form.is_valid(): 
        new_user = form.save()
        login(request, new_user)
        return redirect('learning_log:index')

    context = {'form': form}
    return render(request, 'registration/register/html', context)