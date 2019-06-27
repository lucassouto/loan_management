from rest_framework.routers import SimpleRouter

from .views import ContractViewSet, PaymentViewSet

app_name = 'loans'

router = SimpleRouter()
router.register('contracts', ContractViewSet, basename='contracts')
router.register('payments', PaymentViewSet, basename='payments')

urlpatterns = router.urls
