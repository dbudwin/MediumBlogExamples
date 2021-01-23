from django.urls import path

from . import views

urlpatterns = [
    path("n-plus-one", views.n_plus_1, name="n_plus_1"),
    path("optimized", views.optimized, name="optimized"),
]
