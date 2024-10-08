from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkBoardViewSet, TaskViewSet, UserViewSet
from .auth_views import LoginView, LogoutView, SignUpView

router = DefaultRouter()
router.register(r'workboards', WorkBoardViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]