from rest_framework import serializers
from api.models import User, Blog, Blogslike


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class BlogsLikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogslike
        fields = "__all__"


class BlogsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class UserSubDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_staff", "is_superuser", "is_active"]


class UserSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]


class BlogsSubModelSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()
    author = UserSubSerializer()

    def get_total_likes(self, obj):
        queryset = Blogslike.objects.filter(blog=obj)
        return len(queryset)

    class Meta:
        model = Blog
        fields = [
            "id",
            "author",
            "title",
            "description",
            "content",
            "is_private",
            "total_likes",
        ]
