from django.http import HttpResponse


def index(request):
	return HttpResponse(content_type='text/html', status=200,
						content='<p>You are at the index page</p>')

def entrance(request):
	return
