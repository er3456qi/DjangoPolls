from django.conf.urls import url
from . import views

# set url namespace to avoid {% url %} template tag get confused
# without namespace: {% url 'detail' %}, with namespace {% url 'polls:detail' %}
app_name = 'polls'

"""
    The url() function is passed four arguments,
    two required: regex and view(When Django finds a regular expression match,
    Django calls the specified view function)
    and two optional: kwargs,
    and name(Naming your URL lets you refer to it unambiguously
    from elsewhere in Django especially templates. ).
"""
urlpatterns = [
    # # the 'name' value as called by the {% url %} template tag
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
