from os import name
from django.contrib import admin
from django.urls import path
from user import views as user
from main import views as main
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user.index, name="index"),
    path('join/', user.join, name="join"),
    path('login/', user.userlogin, name="login"),
    path('q/<int:question_id>/', main.q, name="q"),
    path('sight/<int:sight_id>/', main.sight, name="sight_detail"),
    path('home/', main.home, name="home"),
    path('schedule/', main.schedule, name="schedule"),
    path('gym/', main.gym, name="gym"),
    path('sights/', main.sights, name="sights"),
    path('setting/', user.setting, name="setting"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)