from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, OrderItem
from .forms import OrderForm
from .models import Product
from .cart import Cart


def cart_add(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get("quantity", 1))

    cart.add(product, quantity)

    return redirect("cart_detail")


def cart_remove(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)

    return redirect("cart_detail")


def cart_detail(request):
    cart = Cart(request)

    return render(
        request,
        "store/cart_detail.html",
        {
            "cart": cart
        }
    )
def checkout(request):
    cart = Cart(request)

    if len(cart) == 0:
        return redirect("product_list")

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )

            cart.clear()

            return render(
                request,
                "store/order_success.html",
                {
                    "order": order
                }
            )

    else:
        form = OrderForm()

    return render(
        request,
        "store/checkout.html",
        {
            "form": form,
            "cart": cart,
        },
    )