""" views definitions for pages app """
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """ HomePageView definition """
    template_name = 'home.html'
