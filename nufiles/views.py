from django.views import generic
from django.shortcuts import get_object_or_404

from .models import File


class FileList(generic.ListView):
	model = File
	queryset = File.objects.published()
	paginate_by = 10
	template_name = "nufiles/list.html"


class FileDetail(generic.DetailView):
	model = File
	template_name = "nufiles/detail.html"