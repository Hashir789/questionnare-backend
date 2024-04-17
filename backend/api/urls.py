from rest_framework.routers import DefaultRouter
from gennotate.api.urls import user_router, image_router
from django.urls import path, include
router = DefaultRouter()
router.registry.extend(user_router.registry)
router.registry.extend(image_router.registry)
urlpatterns = [
    path('', include(router.urls))
]