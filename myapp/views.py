from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from notifications import notify
from notifications.models import Notification


class NotificationsView(View):
	def get(self, request):
		template = 'myapp/index.html'

		user = request.user
		try:
			unread_notifications = user.notifications.unread()
		except:
			unread_notifications = []

		context = {
			'path': request.path,
			'unread_notifications': unread_notifications,
			'is_user_authenticated': request.user.is_authenticated(),
		}		
		return render(request, template, context)
	def post(self, request):
		password = request.POST['password']
		username = request.POST['username']

		user = authenticate(username=username, password=password)

		if user:
			login(request, user)

		return redirect('myapp:notifications')


class NotifyView(View):
	def get(self, request):
		template = 'myapp/notify.html'

		context = {}
		return render(request, template, context)

	def post(self, request):
		notify.send(request.user, recipient=request.user, verb=request.POST['text'])
		
		return redirect('myapp:notifications')


class ReadNotificationView(View):
	def get(self, request, notification_id):
		notification = Notification.objects.get(id=notification_id)
		notification.mark_as_read()
		
		return redirect('myapp:notifications')