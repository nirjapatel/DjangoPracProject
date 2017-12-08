from django.conf import settings
import re
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
	EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]
	#print(EXEMPT_URLS)

NON_EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_NON_EXEMPT_URLS'):
	NON_EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_NON_EXEMPT_URLS]
	#print(NON_EXEMPT_URLS)
	
class LoginRequiredMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		return response

	def process_view(self, request, view_func, view_args, view_kwargs):
		assert hasattr(request, 'user')
		path = request.path_info.lstrip('/')
		print(path)

		url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
		url_is_not_exempt = any(url.match(path) for url in NON_EXEMPT_URLS)
		

		if path == reverse('logout').lstrip('/'):
			logout(request)

		if request.user.is_authenticated() and url_is_not_exempt:
			#print('Logged in')
			return redirect(settings.LOGIN_REDIRECT_URL)
		elif request.user.is_authenticated() or url_is_exempt:
			#print('Not Logged in')
			return None
		else:
			return redirect(settings.LOGIN_URL)
