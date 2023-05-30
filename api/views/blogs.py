from api.models import Blog, Blogslike
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.serializers import (
    BlogsModelSerializer,
    BlogsSubModelSerializer,
    BlogsLikeModelSerializer,
)


class BlogsModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogsModelSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

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
