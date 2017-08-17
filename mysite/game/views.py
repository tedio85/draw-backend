from django.http import JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie

from game.models import Target

from game.ai import AI

import json

class IndexView(generic.ListView):
	template_name = 'game/index.html'
	context_object_name = 'target_list'

	def get_queryset(self):
		"""
		Return all targets
		"""
		return Target.objects.all()

@csrf_exempt
def entrance(request):
	def get_queryset():
		"""
		Return 2 targets, one for user, one for opponent
		"""
		t1 = Target.objects.order_by('?').first()
		while True:
			t2 = Target.objects.order_by('?').last()
			if t1!=t2:
				break

		return [t1, t2]

	"""
	Return the target when receiving GET requests
	Return the coordinates of a stroke when receiving POST requests
	"""
	data = { }
	if request.method == 'GET':
		queryset = get_queryset()
		data = {
			'targetUser':      queryset[0].target_text,
			'imageUser':       queryset[0].target_img.url,
			'targetOpponent':  queryset[1].target_text,
			'imageOpponent':   queryset[1].target_img.url,
		}

	elif request.method == 'POST':
		data = json.loads(request.body.decode('utf-8'))
		prev_stroke = data[0]['data']['smoothedPointCoordinatePairs']
		data = {
			'stroke':         AI.predict_stroke(prev_stroke)
		}
		response = JsonResponse(data)
		response['Access-Control-Allow-Origin'] = '*'
	return response
