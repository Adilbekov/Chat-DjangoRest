from rest_framework.viewsets import GenericViewSet
from apps.users.permissions import UserPermissons
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import mixins,status
from apps.users.models import User
from apps.users.serializers import UserSerializer, UserRegisterSerializer,UserDetailSerializer

# Create your views here.
class UserViewSet(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action =='create':
            return UserRegisterSerializer
        return UserSerializer
    
    
    def get_serializer_class(self):
        if self.action in ('create', ):
            return UserRegisterSerializer
        if self.action in ('retrieve', ):
            return UserDetailSerializer
        return UserSerializer


    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (UserPermissons(), )
        return (AllowAny(), )



    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'delete' : 'Пользователь успешно удален'}, status=status.HTTP_200_OK)