from django.urls import path

from .views import FeesAddView

urlpatterns = [
    path('fees/add/', FeesAddView.as_view(), name='fees_add'),
]
