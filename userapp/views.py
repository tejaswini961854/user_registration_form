from django.shortcuts import render
from .forms import RegistrationForm

def signup_view(request):
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Check if both passwords match
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password']) # This hashes the password for security
                user.save()
                is_success = True
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form, 'success': is_success})
