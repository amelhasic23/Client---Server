from django.urls import path
from .views import StudentListCreate, StudentRetrieve

urlpatterns = [
    path('students/', StudentListCreate.as_view(), name='student-list-create'),
    path('students/<str:index_number>/', StudentRetrieve.as_view(), name='student-retrieve'),
]
