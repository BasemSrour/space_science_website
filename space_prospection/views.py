from django.views import generic
from .models import Post, Project
from itertools import chain
import random
# from django.shortcuts import get_object_or_404


class HomePageView(generic.ListView):
	template_name = 'space_prospection/index.html'

	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['all_projects'] = Project.objects.all()
		context['all_posts'] = Post.objects.all()
		context['latest_blog'] = Post.objects.all().order_by('-post_pub_date')[:2]
		number_of_posts = Post.objects.count()
		random_index = int(random.random() * number_of_posts) + 1
		context['home_page_pic'] = Post.objects.filter(id=random_index)
		random_index = int(random.random() * number_of_posts) + 1
		context['featured_video_pic'] = Post.objects.filter(id=random_index)
		return context

	def get_queryset(self):
		# Concatenating the querysets into a one list using list(chain(queryset))
		all_posts_and_projects = list(chain(Post.objects.all(), Project.objects.all()))
		return all_posts_and_projects


class ContactView(generic.TemplateView):
	template_name = 'space_prospection/contact_form.html'

	def get_context_data(self, **kwargs):
		context = super(ContactView, self).get_context_data(**kwargs)
		context['all_projects'] = Project.objects.all()
		context['all_posts'] = Post.objects.all()
		return context


class AboutView(generic.TemplateView):
	template_name = 'space_prospection/about.html'

	def get_context_data(self, **kwargs):
		context = super(AboutView, self).get_context_data(**kwargs)
		context['all_projects'] = Project.objects.all()
		context['all_posts'] = Post.objects.all()
		return context


class BlogView(generic.ListView):
	template_name = 'space_prospection/blog.html'

	def get_context_data(self, **kwargs):
		context = super(BlogView, self).get_context_data(**kwargs)
		context['all_projects'] = Project.objects.all()
		context['all_posts'] = Post.objects.all()
		return context

	def get_queryset(self):
		return Post.objects.all()


class ProjectDetailsView(generic.DetailView):
	model = Project
	template_name = 'space_prospection/project_details.html'

	def get_context_data(self, **kwargs):
		context = super(ProjectDetailsView, self).get_context_data(**kwargs)
		context['all_projects'] = Project.objects.all()
		context['all_posts'] = Post.objects.all()
		return context


class ProjectsView(generic.ListView):
	template_name = 'space_prospection/projects.html'

	def get_context_data(self, **kwargs):
		context = super(ProjectsView, self).get_context_data(**kwargs)
		context['all_projects'] = Project.objects.all()
		context['all_posts'] = Post.objects.all()
		return context

	def get_queryset(self):
		return Project.objects.all()


class PostDetailsView(generic.DetailView):
	model = Post
	template_name = 'space_prospection/post_details.html'

	def get_context_data(self, **kwargs):
		context = super(PostDetailsView, self).get_context_data(**kwargs)
		context['all_projects'] = Project.objects.all()
		context['all_posts'] = Post.objects.all()
		return context
