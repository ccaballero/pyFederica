from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('federica.apps.home.views',
        url(r'^$','index', name='home'),
)
