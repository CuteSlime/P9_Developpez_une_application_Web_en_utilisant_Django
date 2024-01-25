from django.views.generic import TemplateView
from django.urls import reverse_lazy


class Flux(TemplateView):
    template_name = "review/flux.html"


class Ticket(TemplateView):
    template_name = "review/ticket.html"


class Ticket_review(TemplateView):
    template_name = "review/ticket_review.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["back_url"] = reverse_lazy("flux")

    #     return context
