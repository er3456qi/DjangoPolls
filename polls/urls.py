from django.conf.urls import url
from . import views

"""
    The url() function is passed four arguments,
    two required: regex and view(When Django finds a regular expression match,
    Django calls the specified view function)
    and two optional: kwargs,
    and name(Naming your URL lets you refer to it unambiguously
    from elsewhere in Django especially templates. ).
"""
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
