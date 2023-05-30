import uuid
from django.db import models
from api.models import User, BaseModel


class Blog(BaseModel):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        unique=True,
    )
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    title = models.CharField(max_length=128)
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title


class Blogslike(BaseModel):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        unique=True,
    )
    post = models.ForeignKey("Blog", on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.liked_by.email} likes {self.post.title}"
