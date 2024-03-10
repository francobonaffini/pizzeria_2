from rest_framework import routers
from .views import PizzasViewSet
from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()

router.register('api/pizzas', PizzasViewSet, 'pizzas')

urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)