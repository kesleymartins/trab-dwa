from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('students/', include('aluno.urls')),
    path('admin/', admin.site.urls),
]
