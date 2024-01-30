from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, serializers
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from apps.chat.permissions import ChatPermissions
from apps.chat.serializers import BackSerializer, FrontSerializer, DataScienceSerializer, MessageSerializer
from apps.chat.models import BackMessage, FrontMessage, DataScienceMessage, Message, User


def index(request):
    return render(request, 'index.html')


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise serializers.ValidationError('Пользователь не аутентифицирован')

        from_user = self.request.user
        to_user_username = self.request.data.get('to_user')
        to_user = get_object_or_404(User, username=to_user_username)

        if from_user == to_user:
            raise serializers.ValidationError('Нельзя отправлять сообщение самому себе')
        
        serializer.save(from_user=from_user, to_user=to_user)





class BackendVievSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = BackMessage.objects.all()
    serializer_class = BackSerializer
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (ChatPermissions(), )
        return (AllowAny(), )

class FrontendVievSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = FrontMessage.objects.all()
    serializer_class = FrontSerializer
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (ChatPermissions(), )
        return (AllowAny(), )

class DateTimeVievSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = DataScienceMessage.objects.all()
    serializer_class = DataScienceSerializer
    permission_classes = (ChatPermissions,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (ChatPermissions(), )
        return (AllowAny(), )