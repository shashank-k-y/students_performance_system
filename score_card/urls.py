from django.urls import path, include

from rest_framework.routers import DefaultRouter

from score_card.views import ScoreView

router = DefaultRouter()
router.register('', ScoreView, basename='student-detail')

urlpatterns = [
    path('detail/', include(router.urls), name='detail'),
]
