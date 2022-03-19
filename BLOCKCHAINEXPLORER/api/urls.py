from rest_framework import routers

from api.views import TransactionViewSet

router = routers.DefaultRouter()
router.register('Transaction', TransactionViewSet)