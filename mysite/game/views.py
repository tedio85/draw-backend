from django.http import HttpResponse
from django.views import generic

from game.models import Target

class IndexView(generic.ListView):
	template_name = 'game/index.html'
	context_object_name = 'target_list'

	def get_queryset(self):
		"""
		Return all targets
		"""
		return Target.objects.all()

class EntranceView(generic.ListView):
	template_name = 'game/entrance.html'
	context_object_name = 'target_list'

	def get_queryset(self):
		"""
		Return 2 targets, one for user, one for opponent
		"""
		t1 = Target.objects.order_by('?').first()
		while True:
			t2 = Target.objects.order_by('?').last()
			if t1!=t2:
				break
		
		return [t1, t2]


