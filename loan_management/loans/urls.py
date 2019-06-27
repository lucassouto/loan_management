from rest_framework.routers import SimpleRouter

from .views import ContractViewSet

app_name = 'loans'

router = SimpleRouter()
router.register('contracts', ContractViewSet, basename='contracts')

urlpatterns = router.urls
