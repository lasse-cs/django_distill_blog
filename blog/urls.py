from django_distill import distill_path
from blog import views


urlpatterns = [
    distill_path("", views.index, name="index", distill_file="index.html"),
]
