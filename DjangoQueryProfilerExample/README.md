# Improving Django Queries Using Django Query Profiler

This code contains the examples outlined in my Medium blog post titled "Improving Django Queries Using Django Query Profiler."  These examples are longform compared to the versions in the blog post.

This repo creates an example Django application with two endpoints.  Both endpoints accomplish the same thing, but one has been optimized to eliminate N+1 queries.

## Getting Started

This example project uses [`poetry`](https://python-poetry.org/) to install and manage dependencies.  You'll also need Chrome and the [Django Query Profiler extension](https://chrome.google.com/webstore/detail/django-query-profiler/ejdgfhecpkhdnpdmdheacfmknaegicff).

1. `poetry install`
2. `python manage.py migrate`
3. `python manage.py loaddata db_data.json`
4. `python manage.py runserver`
5. Visit either `http://127.0.0.1:8000/blogs/n-plus-one` or `http://127.0.0.1:8000/blogs/optimized` and view the results in the "Django Query Profiler" tab in Chrome's Developer Tools
