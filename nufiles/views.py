from django.views import generic
from django.shortcuts import get_object_or_404

from .models import File


class FileList(generic.ListView):
	model = File
	queryset = File.objects.published()
	paginate_by = 10
	template_name = "nufiles/list.html"

	def get_queryset(self):
		queryset = super(FileList, self).get_queryset()
		if not self.request.user.is_authenticated():
			queryset = File.objects.public()
		return queryset


class FileDetail(generic.DetailView):
	model = File
	template_name = "nufiles/detail.html"