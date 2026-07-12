from django.urls import path
from . import views, cart_views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path(
        'category/<slug:category_slug>/',
        views.product_list,
        name='product_list_by_category'
    ),
    path(
        'product/<slug:slug>/',
        views.product_detail,
        name='product_detail'
    ),

    # Cart URLs
    path(
        'cart/',
        cart_views.cart_detail,
        name='cart_detail'
    ),
    path(
        'cart/add/<int:product_id>/',
        cart_views.cart_add,
        name='cart_add'
    ),
    path(
        'cart/remove/<int:product_id>/',
        cart_views.cart_remove,
        name='cart_remove'
    ),
    path(
    "checkout/",
    cart_views.checkout,
    name="checkout",
),
]