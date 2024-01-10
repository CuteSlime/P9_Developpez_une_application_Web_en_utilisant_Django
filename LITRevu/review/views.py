from django.views.generic import TemplateView
from django.urls import reverse_lazy


class Index(TemplateView):
    template_name = "review/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["back_url"] = reverse_lazy("index")

        return context
