from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('create-checkout-session/<int:product_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
]
