from django.shortcuts import render

from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):  # платежи

    serializer = PaymentSerializer
    queryset = Payment.objects.all()  # список платежей
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # фильтры
    filterset_fields = ('course', 'lesson', 'payment_method')  # поля фильтрации
    ordering_fields = ('date_of_payment',)  # Поля сортировки
    permission_classes = [IsAuthenticated]
