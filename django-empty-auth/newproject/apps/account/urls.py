from django.core.urlresolvers import reverse_lazy
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from forms import CustomAuthenticationForm

urlpatterns = patterns('',
    url(r'^logout$',
        logout,
        {'next_page': reverse_lazy('homepage')},
        name='logout'),
    url(r'^login$',
        login,
        {'template_name': 'account/login.html',
        'authentication_form': CustomAuthenticationForm}, 
        name='login'),
    url(r'^password-change/$',
        'django.contrib.auth.views.password_change',
        {'template_name': 'account/password_change.html',
         'post_change_redirect': reverse_lazy('homepage')}, 
        name='password-change'),
)
