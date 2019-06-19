from rest_framework.routers import SimpleRouter

from .views import BankViewSet

app_name = 'banks'

router = SimpleRouter()
router.register('banks', BankViewSet, basename='banks')

urlpatterns = router.urls
