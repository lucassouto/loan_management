from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken

from .views import HealthCheck

app_name = 'api'

router = SimpleRouter()
router.register('health-check', HealthCheck, basename='health_check')

schema_view = get_schema_view(
    openapi.Info(
        title="Loan Management API",
        default_version='v1',
        description="Loan Management Documentation",
        contact=openapi.Contact(email="lucasinfologos@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(
        r'^docs(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('obtain-token/', ObtainJSONWebToken.as_view(), name='obtain_token'),
    path('refresh-token/', RefreshJSONWebToken.as_view(), name='refresh_token'),
    path('verify-token/', VerifyJSONWebToken.as_view(), name='verify_token'),
    path('', include('loan_management.users.urls')),
    path('', include('loan_management.banks.urls')),
    path('', include('loan_management.loans.urls')),
]

urlpatterns += router.urls
