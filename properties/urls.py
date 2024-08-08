from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PropertiesEndpoint,SpecificPropertyEndpoint,SpecificPropertyImagesEndpoint

urlpatterns=[
    path('',PropertiesEndpoint.as_view()),
    path('<int:id>/',SpecificPropertyEndpoint.as_view()),
    path('images/<int:id>',SpecificPropertyImagesEndpoint.as_view())
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
