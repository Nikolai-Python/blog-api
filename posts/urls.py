from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewSet, CommentViewSet, CategoryViewSet



router = SimpleRouter()

router.register('users', UserViewSet, basename='users')
router.register('comments', CommentViewSet, basename='comments')
router.register('categories', CategoryViewSet, basename='categories')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls
