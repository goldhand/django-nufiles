from django.conf.urls import patterns, url

from .views import FileList, FileDetail


urlpatterns = patterns('',
	url(r'^$', FileList.as_view(), name='list'),
	# allows slugs to contain [_, -]
	#url(r'^(?P<slug>[-_\w]+)/$', FileDetail.as_view(), name='detail'),
	# allows anything to be a slug
	url(r'^(?P<slug>.*)/$', FileDetail.as_view(), name='detail'),
	
)