from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count
from .forms import LoginForm, UserRegistrationForm
from .models import Product, Category


def product_list(request, category_slug=None):
    query = request.GET.get("q")
    selected_category = None

    products = Product.objects.filter(available=True)

    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    categories = Category.objects.annotate(
        product_count=Count('products', filter=Q(products__available=True))
    ).order_by('name')

    return render(
        request,
        "store/product_list.html",
        {
            "products": products,
            "query": query,
            "categories": categories,
            "selected_category": selected_category,
        },
    )


def product_detail(request, slug):
    product = get_object_or_404(
        Product,
        slug=slug,
        available=True
    )

    return render(
        request,
        'store/product_detail.html',
        {'product': product}
    )


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()

    return render(request, "store/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "store/profile.html", {"user": request.user})
