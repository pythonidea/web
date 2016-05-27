from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'qa.views.test'),
    url(r'^login/$', 'qa.views.test'),
    url(r'^signup/$', 'qa.views.test'),
    url(r'question/(?P<id>\d+)/$', one_question, name='question'),
    url(r'^ask/.*$', 'qa.views.test'),
    url(r'popular/$', popular_questions, name='popular'),
    url(r'new/$', new_questions, name='new'),
)
