from django.urls import path
from payment.views import GetBalanceAPI, UpdateBalanceAPI, GetTransactionsAPI

urlpatterns = [
    path("get_balance/", GetBalanceAPI.as_view(), name="get_balance"),
    path("update_balance/", UpdateBalanceAPI.as_view(), name="update_balance"),
    path("get_transactions/", GetTransactionsAPI.as_view(), name="get_transactions"),
]
