from api.v1.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                          ReviewViewSet, TitleViewSet, UsersViewSet,
                          APIGetToken, APISignup)
from django.urls import include, path
from rest_framework.routers import SimpleRouter

router_v1 = SimpleRouter()

router_v1.register(r'titles', TitleViewSet)
router_v1.register(r'categories', CategoryViewSet)
router_v1.register(r'genres', GenreViewSet)
router_v1.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet,
                   basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')
router_v1.register('users', UsersViewSet, basename='users')


jwt_patterns = [
    path('token/', APIGetToken.as_view(), name='get_token'),
    path('signup/', APISignup.as_view(), name='signup'),
]

urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include(jwt_patterns)),
]
