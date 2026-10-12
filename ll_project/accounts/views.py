from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from .forms import CleanUserCreationForm


def register(request):
    """Register a new user."""
    if request.method != "POST":
        # Display blank registration form.
        form = CleanUserCreationForm()
    else:
        # Process completed form.
        form = CleanUserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect("learning_logs:index")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "registration/register.html", context)


class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)


# 1. login
# 2. permanent delete account
# 3. change account password
# 4. change username
