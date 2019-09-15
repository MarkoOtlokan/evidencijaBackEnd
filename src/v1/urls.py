from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import *
router = DefaultRouter()

router.register(r'proizvod',ProizvodViewSet)
router.register(r'radnik',RadnikViewSet)
router.register(r'klijent',KlijentViewSet)
router.register(r'usluga',UslugaViewSet)

urlpatterns = [
    url(r'',include(router.urls)),

]
