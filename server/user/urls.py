from django.urls import path
from user.views import loginView, registerView, CookieTokenRefreshView, logoutView, user, getSubscriptions
from . import views

app_name = "user"

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('login', loginView),
    path('register', registerView),
    path('refresh-token', CookieTokenRefreshView.as_view()),
    path('logout', logoutView),
    path('user', user),
    path('subscriptions', getSubscriptions)
]
