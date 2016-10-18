from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'path',views.viewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]
