from django.http import HttpResponse

from blogs.models import Comment


def n_plus_1(request):
    comments = Comment.objects.all()

    for comment in comments:
        print(comment.post.title)

    return HttpResponse("N+1")


def optimized(request):
    comments = Comment.objects.all().select_related("post")

    for comment in comments:
        print(comment.post.title)

    return HttpResponse("Optimized")
