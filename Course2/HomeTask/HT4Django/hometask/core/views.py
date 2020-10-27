from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView
from core.models import Guilds


class IndexView(TemplateView):
    template_name = "index.html"


class CreateGuildView(CreateView):
    template_name = "create_guild.html"
    model = Guilds
    fields = '__all__'
    success_url = '/'


class UpdateGuildView(UpdateView):
    template_name = "create_guild.html"
    model = Guilds
    fields = '__all__'
    success_url = '/'
