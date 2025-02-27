from django.urls import path
from .user.views import LoginView, SignupView, UserProfileView
from .views import main, authors, get_author, create_author, delete_author, update_author, courses, create_course, update_course, get_course, delete_course
from .user.google import GoogleLoginView


urlpatterns = [
    path('', main, name="autho"),
    path('author/', authors, name="All authors"),
    path('author/<uuid:id>', get_author, name="authors"),
    path('author/create', create_author, name="create author"),
    path('author/delete/<uuid:id>', delete_author, name="delete author"),
    path('author/update/<uuid:id>', update_author, name="update author"),
    path('course/', courses, name="All courses"),
    path('course/<uuid:id>', get_course, name="course"),
    path('course/create', create_course, name="create course"),
    path('course/delete/<uuid:id>', delete_course, name="delete course"),
    path('course/update/<uuid:id>', update_course, name="update course"),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path("google/auth/", GoogleLoginView.as_view(), name="google auth"),
]