from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ticket, Review
from django.contrib.auth.mixins import LoginRequiredMixin

# Flux


class TicketListView(ListView):
    model = Ticket
    template_name = "review/flux.html"


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = "review/ticket_new.html"
    success_url = reverse_lazy("flux")
    fields = (
        "title",
        "description",
        "image",
    )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Ticket


class TicketDetailView(DetailView):
    model = Ticket
    template_name = "review/ticket.html"


class TicketUpdateView(UpdateView):
    model = Ticket
    success_url = reverse_lazy("flux")
    template_name = "review/ticket_update.html"
    fields = (
        "title",
        "description",
        "image",
    )


class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = "review/ticket_delete.html"
    success_url = reverse_lazy("flux")


# create and review a ticket at the same time
class TicketReviewCreateView(CreateView):
    template_name = "review/ticket_review_new.html"
    success_url = reverse_lazy("flux")


# review
class ReviewCreateView(CreateView):
    model = Review
    template_name = "review/review_new.html"

    fields = (
        "headline",
        "body",
        "rating",
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket = self.kwargs['ticket_id']
        print(ticket)
        context["ticket"] = Ticket.objects.get(pk=ticket)

        return context

    def form_valid(self, form):
        form.instance.ticket = get_object_or_404(
            Ticket, pk=self.kwargs['ticket_id'])
        form.instance.user = self.request.user
        form.instance.rating = form.cleaned_data['rating']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ticket', kwargs={'pk': self.object.ticket.pk})


class ReviewListView(ListView):
    model = Review
    template_name = "review/flux.html"


class ReviewUpdateView(UpdateView):
    model = Review
    template_name = "review/review_update.html"
    fields = (
        "headline",
        "body",
        "rating",
    )

    def get_success_url(self):
        return reverse_lazy('ticket', kwargs={'pk': self.object.ticket.pk})


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = "review/review_delete.html"

    def get_success_url(self):
        return reverse_lazy('ticket', kwargs={'pk': self.object.ticket.pk})
