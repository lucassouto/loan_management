from rest_framework.routers import SimpleRouter

from .views import UsersViewSet

app_name = 'users'

router = SimpleRouter()
router.register('users', UsersViewSet, basename='users')

urlpatterns = router.urls
