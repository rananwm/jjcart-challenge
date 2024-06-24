from django.urls import path
from transaction.views import paySubscription, listSubscriptions
from . import views

app_name = "transaction"

urlpatterns = [
    path('transactions/', views.TransactionListView.as_view(), name='transaction-list'),
    path('pay', paySubscription),
    path('list', listSubscriptions)
]
