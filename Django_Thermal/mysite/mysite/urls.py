from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings
from members import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.login, name="login"),
    path('', include('members.urls')),
    path('', include('index.urls')),
    path('charts', include('charts.urls')),
    path('tables', include('tables.urls')),
    path('imgs', include('imgs.urls')),
    path('django_plotly_dash', include('django_plotly_dash.urls')),
    path('signup',views.signup, name="signup"),
    url('members/', include('django.contrib.auth.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)