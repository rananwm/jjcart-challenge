from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Rana NWM Documentation",
      default_version='v1',
      description="API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="email@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user.urls', namespace='user')),
    path('transaction/', include('transaction.urls', namespace='transaction')),
    path('hello_world/', include('hello_world.urls', namespace='hello_world')),
    path('hello_universe/', include('hello_universe.urls', namespace='hello_universe')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
