from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from sales.views import LandingPageView, home_page ,SignupView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name = 'home-page'),
    path('sales/', include('sales.urls', namespace="sales")),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)