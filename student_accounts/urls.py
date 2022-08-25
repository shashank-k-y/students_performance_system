from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from student_accounts import views

router = DefaultRouter()
router.register('', views.StudentDetailsView, basename='student-detail')

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.registration_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('detail/', include(router.urls)),
]
