from django.contrib.auth.models import User

from rest_framework import viewsets

from .models import Post, Comment, Category
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer,\
            CommentSerializer, CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Comment.objects.all()  
    serializer_class = CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
