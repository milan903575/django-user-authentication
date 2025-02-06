from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.urls import reverse
from django.http import HttpResponseBadRequest
from .forms import SignUpForm  # Custom signup form
from django.conf import settings  # Ensure email settings are configured


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully! You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()

    return render(request, 'user_authentication/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        # Check if input is email
        user = User.objects.filter(email=username_or_email).first()
        if user:
            username = user.username  # Get the username from the email
        else:
            username = username_or_email  # Assume input is username

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'user_authentication/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

# Dashboard View (Protected)
@login_required
def dashboard_view(request):
    return render(request, 'user_authentication/dashboard.html', {'username': request.user.username})

# Profile View (Protected)
@login_required
def profile_view(request):
    return render(request, 'user_authentication/profile.html', {'user': request.user})

# Change Password (Protected)
@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevents logout after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'user_authentication/change_password.html', {'form': form})


def forgot_password_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()

            if user:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_url = request.build_absolute_uri(reverse('reset_password', args=[uid, token]))

                email_subject = "Password Reset Request"
                email_body = render_to_string('user_authentication/password_reset_email.html', {'reset_url': reset_url})

                send_mail(email_subject, email_body, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)
                messages.success(request, 'Password reset instructions have been sent to your email.')
                return redirect('login')
            else:
                messages.error(request, 'No account found with this email.')

    else:
        form = PasswordResetForm()

    return render(request, 'user_authentication/forgot_password.html', {'form': form})


def reset_password_view(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError):
        return HttpResponseBadRequest("Invalid link")

    if not default_token_generator.check_token(user, token):
        return HttpResponseBadRequest("Invalid or expired token")

    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep user logged in after password reset
            messages.success(request, 'Your password has been reset successfully!')
            return redirect('login')

    else:
        form = SetPasswordForm(user)

    return render(request, 'user_authentication/reset_password.html', {'form': form})
