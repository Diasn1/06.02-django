from django.urls import path
from .views import (
    AnimalListView, AnimalDetailView, AnimalCreateView,
    AnimalUpdateView, AnimalDeleteView, EnclosureListView,
    EnclosureDetailView, EnclosureCreateView, EnclosureUpdateView,
    EnclosureDeleteView
)

urlpatterns = [
    path('animals/', AnimalListView.as_view(), name='animal_list'),
    path('animals/<int:pk>/', AnimalDetailView.as_view(), name='animal_detail'),
    path('animals/create/', AnimalCreateView.as_view(), name='animal_create'),
    path('animals/<int:pk>/update/', AnimalUpdateView.as_view(), name='animal_update'),
    path('animals/<int:pk>/delete/', AnimalDeleteView.as_view(), name='animal_delete'),
    path('enclosures/', EnclosureListView.as_view(), name='enclosure_list'),
    path('enclosures/<int:pk>/', EnclosureDetailView.as_view(), name='enclosure_detail'),
    path('enclosures/create/', EnclosureCreateView.as_view(), name='enclosure_create'),
    path('enclosures/<int:pk>/update/', EnclosureUpdateView.as_view(), name='enclosure_update'),
    path('enclosures/<int:pk>/delete/', EnclosureDeleteView.as_view(), name='enclosure_delete'),
]