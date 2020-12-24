"""generate_teachers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Api.views import GroupViewSet, StudentViewSet, TeacherViewSet

import debug_toolbar

from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include(("core.urls", "core"), namespace='students')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls))  # best api way
    # path('api/v1/students/', StudentViewSet.as_view({'get': 'list'})) # first api method # noqa
    # path('BlueRam/', include("core.urls")), # можно добавить префикс
]
