from django.contrib import admin
from django.urls import path, include

from .views import SaveStatView, GetStatView, DeleteStatView

urlpatterns = [
    path('save/', SaveStatView.as_view()),
    path('get/<str:order_by>/', GetStatView.as_view()),
    path('delete/', DeleteStatView.as_view()),
]
