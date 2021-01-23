from django.urls import include, path

urlpatterns = [
    path("django_query_profiler/", include("django_query_profiler.client.urls")),
    path("blogs/", include("blogs.urls")),
]
