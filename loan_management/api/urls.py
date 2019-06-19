from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken
from .views import HealthCheck


app_name = 'api'

router = SimpleRouter()
router.register('health-check', HealthCheck, basename='health_check')

urlpatterns = [
    path('obtain-token/', ObtainJSONWebToken.as_view(), name='obtain_token'),
    path('refresh-token/', RefreshJSONWebToken.as_view(), name='refresh_token'),
    path('verify-token/', VerifyJSONWebToken.as_view(), name='verify_token'),
    path('', include('loan_management.users.urls')),
    path('', include('loan_management.banks.urls')),
]

urlpatterns += router.urls
