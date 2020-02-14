from .views import AddNewHouse, AddBrickworkTask, AllStatistics
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('building/', AddNewHouse.as_view()),
    path('building/<int:id>/add-bricks/', AddBrickworkTask.as_view()),
    path('stats/', AllStatistics.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)