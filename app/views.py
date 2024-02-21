from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required


# - Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout




# main contents start here_____________________________________________________________________________________________________________________



class home(ListView):
    context_object_name = "categories"
    template_name = 'index.html'

    def get_queryset(self):
        return category.objects.filter(status=0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_product'] = product.objects.filter(is_new=True)
        context['trending_products'] = product.objects.filter(trending=True)
        return context

def store(request, slug):
    # Use get_object_or_404 to raise a 404 error if the category is not found
    category_instance = get_object_or_404(category, slug=slug, status=0)

    # Use related_name to fetch products for a category
    products = category_instance.product_set.all()

    context = {'products': products, 'category_name': category_instance}
    return render(request, 'store.html', context)

def product_detail(request, category_slug, product_slug):

    if (category.objects.filter(slug=category_slug, status=0)):
        if(product.objects.filter(slug=product_slug, status=0)):
            proo = product.objects.filter(slug=product_slug, status=0).first

            context = {'proo': proo}
        else:
            messages.error(request,'no such product found')
            return redirect('product_detail')
    else:
        messages.error(request, 'no such category found')
        return redirect('product_detail')
    return render(request, 'product.html', context)


def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request,'Registeration Succesful login to continue')

            return redirect("login")


    context = {'form':form}

    return render(request, 'register.html', context=context)

def login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)
                messages.success(request, 'Wellcome back ')

                return redirect("home")


    context = {'form':form}

    return render(request, 'login.html', context=context)
