from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})



def register(request):
    form = UserRegistrationForm() 
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user = new_user)
            return render(request, 'account/register_done.html',{'new_user': new_user})
    
        
    return render(request,'account/register.html',{"form":form})



@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile, files=request.FILES)

    return render(request, 'account/edit.html', {"user_form": user_form, "profile_form": profile_form})
