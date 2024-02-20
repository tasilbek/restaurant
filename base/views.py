from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class MenuPageView(TemplateView):
    template_name = 'pages/menu.html'

class PagesView(TemplateView):
    template_name = 'pages/pages.html'

class BookPageView(TemplateView):
    template_name = 'pages/book.html'

class TeamPageView(TemplateView):
    template_name = 'pages/team.html'

class TestimonialPageView(TemplateView):
    template_name = 'pages/testimonial.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

class ServicePageView(TemplateView):
    template_name = 'pages/service.html'