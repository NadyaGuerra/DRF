from django.urls import path
from payment.apps import PaymentConfig
from payment.views import PaymentListAPIView

app_name = PaymentConfig.name

urlpatterns = [
     path('payment/', PaymentListAPIView.as_view(), name='payment'),
 ]