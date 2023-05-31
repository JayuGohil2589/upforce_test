from api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()

router.register("users", views.UserModelViewSet, basename="users")
router.register("blogs", views.BlogsModelViewSet, basename="blogs")
router.register("blogs-like", views.BlogsLikeModelViewSet, basename="blogs-like")

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
    path("gettoken/", TokenObtainPairView().as_view(), name="gettoken"),
]
