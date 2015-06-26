from django.conf.urls import patterns, include, url
from django.contrib import admin
import notifications


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_notifications_example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('myapp.urls', namespace="myapp")),
	url(r'^inbox/notifications/', include(notifications.urls)),
)
