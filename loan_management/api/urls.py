from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken
from .views import HealthCheck


app_name = 'api'

router = SimpleRouter()
router.register('health-check', HealthCheck, basename='health_check')

urlpatterns = [
    path('obtain-token/', ObtainJSONWebToken.as_view()),
    path('refresh-token/', RefreshJSONWebToken.as_view()),
    path('verify-token/', VerifyJSONWebToken.as_view()),
]

urlpatterns += router.urls
