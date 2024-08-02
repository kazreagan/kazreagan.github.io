import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from timeless.models import Product
from .models import Order

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request, product_id):
    product = Product.objects.get(id=product_id)
    session = stripe.checkout.Session.create(payment_method_types=['card'], line_items=[{
        'price_data': {
            'currency': 'usd',
            'product_data': {
                'name': product.name,
            },
            'unit_amount': int(product.price * 100),
        },
        'quantity': 1,
    }],
    mode='payment',
    success_url=request.build_absolute_url('/payment/success/'),
    cancel_url=request.build_absolute_url('/payment/success'),
    )
    order = Order.objects.create(
        user=request.user, product=product,
        stripe_payment_intent=session.payment_intent,
        amount=product.price
    )
    return redirect(session.url, code=303)

def payment_success(request):
    return render(request, 'payment/success.html')

def payment_cancel(request):
    return render(request, 'payment/cancel.html')