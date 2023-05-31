from api.models import Blog, Blogslike
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.serializers import (
    BlogsModelSerializer,
    BlogsSubModelSerializer,
    BlogsLikeModelSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.custompermissions import (
    isPrivateBlogsAccessible,
    isReadWriteUpdateDeletePermitted,
    isReadAndCreateAndDeleteOnlyPermitted,
)


class BlogsModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogsModelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        IsAuthenticated,
        isPrivateBlogsAccessible,
        isReadWriteUpdateDeletePermitted,
    ]

    def list(self, request, *args, **kwargs):
        queryset = Blog.objects.filter(is_private=False)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = BlogsSubModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BlogsSubModelSerializer(instance)
        return Response(serializer.data)


class BlogsLikeModelViewSet(ModelViewSet):
    queryset = Blogslike.objects.all()
    serializer_class = BlogsLikeModelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, isReadAndCreateAndDeleteOnlyPermitted]
