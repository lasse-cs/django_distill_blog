from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><head><title>Test Title</title></head></html>")
