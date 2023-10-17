from django.urls import path
from .views import  SBCReportView

urlpatterns = [
    path('create/', SBCReportView.as_view(), name='create-sbc-report'),

]
