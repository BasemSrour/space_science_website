from django.conf.urls import url
from . import views

app_name = 'space_prospection'

urlpatterns = [
	# /space/
	url(r'^$', views.HomePageView.as_view(), name='home'),
	# /space/contact/
	url(r'^contact/$', views.ContactView.as_view(), name='contact'),
	# /space/about/
	url(r'^about/$', views.AboutView.as_view(), name='about'),
	# /space/blog/
	url(r'^blog/$', views.BlogView.as_view(), name='blog'),
	# /space/project/<pk>/detials/
	url(r'^project/(?P<pk>[0-9]+)/details/$', views.ProjectDetailsView.as_view(), name='project_details'),
	# /space/projects/
	url(r'^projects/$', views.ProjectsView.as_view(), name='projects'),
	# /space/post/<pk>/details/
	url(r'^post/(?P<pk>[0-9]+)/details/$', views.PostDetailsView.as_view(), name='post_details'),
]
