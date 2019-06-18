from rest_framework.routers import SimpleRouter
from .views import HealthCheck


app_name = 'api'

router = SimpleRouter()
router.register('health-check', HealthCheck, base_name='health_check')

urlpatterns = router.urls
