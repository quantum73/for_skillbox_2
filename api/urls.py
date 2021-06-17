from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'directions', views.DirectionsViewSet)
router.register(r'courses', views.CoursesViewSet)
router.register(r'lessons', views.LessonsViewSet)
router.register(r'lesson-materials', views.LessonMaterialsViewSet)
urlpatterns = router.urls
