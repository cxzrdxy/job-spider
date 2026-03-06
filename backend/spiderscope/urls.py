"""
URL configuration for spiderscope project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import SpiderTaskViewSet

# 1. 创建 DRF 路由器
router = DefaultRouter()
router.register(r'tasks', SpiderTaskViewSet)  # 这会生成 /api/tasks/ 的 CRUD 接口

urlpatterns = [
    path('admin/', admin.site.urls),

    # 2. 将路由器的 URL 包含进来
    path('api/', include(router.urls)),

    # 3. JWT 认证接口
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
