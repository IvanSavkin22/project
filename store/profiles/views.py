from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth import authenticate, login as login_user, logout as logout_user, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import LoginForm, RegisterForm, ChangePasswordForm
from store.product.models import *
from store.servicer.models import *
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ProfileView(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def get_basket(self):
        return Purchase.objects.filter(user=self.user)

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} purchased {self.content_object}"


def login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                login_user(request, user)
                return redirect('home')

    return render(request, 'profiles/login.html', {"login_form": form})


@login_required
def home(request):

    return render(request, 'profiles/home.html')


@login_required
def logout(request):
    logout_user(request)
    return redirect('main')


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password_one')

            User = get_user_model()
            User.objects.create_user(username=username, password=password)
            user = authenticate(request, username=username, password=password)

            login_user(request, user)

            return redirect('home')

    return render(request, 'profiles/register.html', {"form": form})


@login_required
def change_password(request):
    form = ChangePasswordForm()

    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('password_one')

            request.user.set_password(new_password)
            request.user.save()

            update_session_auth_hash(request, request.user)

            return redirect('change_password_success')

    return render(request, 'profiles/change_password.html',  {"form": form})

@login_required
def change_password_success(request):
    return render(request, 'profiles/change_password_success.html')


@login_required
def profile_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if product not in request.user.profile.get_products():
        raise Http404

    return render(request, 'profiles/profile_product.html', {'product': product})

