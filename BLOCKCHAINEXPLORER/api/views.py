from rest_framework import viewsets

from api.models import Transaction
from api.serializers import TransactionSerializers

class TransactionViewSet(viewsets.ModelViewSet):

    queryset = Transaction.objects.all()
    serializers_class = TransactionSerializers