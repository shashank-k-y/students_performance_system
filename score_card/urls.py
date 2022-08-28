from django.urls import path, include

from rest_framework.routers import DefaultRouter

from score_card import views

router = DefaultRouter()
router.register('', views.ScoreView, basename='student-detail')

urlpatterns = [
    path('detail/', include(router.urls), name='detail'),
    path(
        'performance/<str:subject>',
        views.IndividualPerformance.as_view(),
        name="performance"
    ),
    path(
        'overall-performance/', views.OverallPerformance.as_view(),
        name="overall-performance"
    )
]
