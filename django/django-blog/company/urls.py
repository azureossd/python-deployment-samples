from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
