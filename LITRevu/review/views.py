from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ticket, Review

# Flux


class TicketListView(ListView):
    model = Ticket
    template_name = "review/flux.html"


class TicketCreateView(CreateView):
    model = Ticket
    template_name = "review/ticket_create.html"

# Ticket


class TicketDetailView(DetailView):
    model = Ticket
    template_name = "review/ticket.html"


class TicketUpdateView(UpdateView):
    model = Ticket
    fields = (
        "title",
        "description",
        "image",
    )
    template_name = "review/ticket_update.html"


class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = "review/ticket_delete.html"
    success_url = reverse_lazy("flux")

# create and review a ticket at the same time


class TicketReviewCreateView(CreateView):
    template_name = "review/ticket_review_create.html"


# review
class ReviewCreateView(CreateView):
    template_name = "review/review_create.html"


class ReviewListView(ListView):
    model = Review
    template_name = "review/flux.html"


class ReviewUpdateView(UpdateView):
    model = Review
    fields = (
        "title",
        "description",
        "image",
    )
    template_name = "review/review_update.html"


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = "review/review_delete.html"
    success_url = reverse_lazy("flux")

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["back_url"] = reverse_lazy("flux")

    #     return context
