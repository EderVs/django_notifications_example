from django.conf.urls import patterns, include, url

from .views import NotificationsView, NotifyView, ReadNotificationView


urlpatterns = patterns('',

	url(
		r'^$',
		NotificationsView.as_view(),
		name='notifications'
    ),
    url(
		r'^notify/',
		NotifyView.as_view(),
		name='notify'
    ),
    url(
    	r'^read/(?P<notification_id>\d+)/$',
    	ReadNotificationView.as_view(),
    	name='read'
    ),
    url(
		r'^logout/$',
		'django.contrib.auth.views.logout',
	),
)
