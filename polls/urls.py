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
    url(r'^$', views.index, name='index')
]
