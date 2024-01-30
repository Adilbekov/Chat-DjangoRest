from django.urls import path, include
from rest_framework import routers

from apps.chat import consumers
from .views import MessageCreateView, BackendVievSet, FrontendVievSet, DateTimeVievSet
from apps.chat.views import index

router = routers.DefaultRouter()
router.register('backend', BackendVievSet, basename='backend_api')
router.register('frontend', FrontendVievSet, basename='frontend_api')
router.register('datetime', DateTimeVievSet, basename='datetime_api')


urlpatterns = [
    path('', index, name='rooms'),
    path('chat', include(router.urls)),
    path('messages/', MessageCreateView.as_view(), name='message-list'),
]