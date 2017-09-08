import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Project(models.Model):
	proj_title = models.CharField(max_length=100)
	proj_pic = models.ImageField(null=True)
	proj_content = HTMLField()
	proj_is_featured = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('space_prospection:project_details', kwargs={'pk': self.pk})

	def __str__(self):
		return self.proj_title


class Post(models.Model):
	post_pic = models.ImageField(null=True)
	post_title = models.CharField(max_length=100)
	post_pub_date = models.DateTimeField('date published')
	post_content = HTMLField()
	post_is_featured = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('space_prospection:post_details', kwargs={'pk': self.pk})

	def was_published_recently(self):
		return self.post_pub_date >= timezone.now() - datetime.timedelta(days=1)

	def __str__(self):
		return self.post_title
