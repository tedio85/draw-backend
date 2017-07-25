from django.db import models
from django.utils.html import mark_safe
from django.contrib.staticfiles.templatetags.staticfiles import static

import re

class Target(models.Model):
	target_num = models.IntegerField(primary_key=True)
	target_text = models.CharField(max_length=200)
	target_img = models.ImageField(upload_to='static/game/images/')
	
	def image_tag(self):
		url = re.sub("static","",self.target_img.url)
		url = static(url)
		return mark_safe('<img src="%s". width="150" height="150" />' % (url))

	image_tag.short_description = 'Image'