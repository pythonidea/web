from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from qa.views import test, new_questions, popular_questions, one_question


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'qa.views.new_questions'),
    url(r'^login/$', 'qa.views.test'),
    url(r'^signup/$', 'qa.views.test'),
    url(r'question/(?P<id>\d+)/$', 'qa.views.one_question', name='question'),
    url(r'^ask/.*$', 'qa.views.test'),
    url(r'popular/$', 'qa.views.popular_questions', name='popular'),
    url(r'new/$', 'qa.views.new_questions', name='new'),
)
