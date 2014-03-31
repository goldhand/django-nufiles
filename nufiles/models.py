# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel, ActivatorModel

from .managers import FileManager


class File(TimeStampedModel, TitleSlugDescriptionModel, ActivatorModel):
	file = models.FileField(upload_to='nufiles/files/%Y/%m/%d')
	img = models.ImageField(upload_to='nuFiles/thumbs/%Y/%m/%d', blank=True)

	objects = FileManager()

	class Meta:
		verbose_name = _('File')
		verbose_name_plural = _('Files')
		ordering = ('-created',)

	def __unicode__(self):
		return u'%s' % self.title

	def get_absolute_url(self):
		return reverse('nufiles:detail', kwargs={'slug': self.slug})