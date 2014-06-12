from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from newproject.apps.main.views import MainPageView
from newproject.apps.account.views import CustomRegistrationView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', MainPageView.as_view(), name='homepage'),
    url(r'^register/$',
        CustomRegistrationView.as_view(),
        name='register'),
    url(r'^register/complete/$',
        TemplateView.as_view(template_name='registration/registration_complete.html'),
        name='registration_complete'),
    url(r'^register/closed/$',
        TemplateView.as_view(template_name='registration/registration_closed.html'),
        name='registration_disallowed'),
    url(r'^account/', include('newproject.apps.account.urls', namespace='account')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*', include('newproject.apps.main.urls', namespace='main'))
)

urlpatterns += patterns(
    'django.views.static',
    (
        r'^static/(?P<path>.*)$',
        'serve',
        {
            'document_root': 'newproject/static/',
            'show_indexes': True
        }
    ))
urlpatterns += patterns(
    'django.views.static',
    (
        r'^media/(?P<path>.*)$',
        'serve',
        {
            'document_root': 'newproject/media/',
            'show_indexes': True
        }
    ))