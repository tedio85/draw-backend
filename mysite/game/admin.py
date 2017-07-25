from django.contrib import admin

from .models import Target

class TargetAdmin(admin.ModelAdmin):
	fields = ['target_num', 'target_text', 'target_img', 'image_tag']
	readonly_fields = ('image_tag',)

	list_display = ('target_num', 'target_text')

admin.site.register(Target, TargetAdmin)
