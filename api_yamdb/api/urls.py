from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import TitleViewSet, ReviewViewSet, CommentViewSet, UsersViewSet, signup_user, create_token


router_v1 = DefaultRouter()

# http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
# http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
router_v1.register('titles/(?P<titles_id>\\d+)/reviews', ReviewViewSet,
                   basename='reviews')

# http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
# http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
router_v1.register(
    'titles/(?P<titles_id>\\d+)/reviews/(?P<review_id>\\d+)/comments',
    CommentViewSet,
    basename='reviews'
)
router_v1.register('titles', TitleViewSet)
router_v1.register('users', UsersViewSet, basename='users')

urlpatterns = [
    path('v1/auth/signup/', signup_user, name='signup'),
    path('v1/auth/token/', create_token, name='token'),
    path('v1/', include(router_v1.urls)),
]
