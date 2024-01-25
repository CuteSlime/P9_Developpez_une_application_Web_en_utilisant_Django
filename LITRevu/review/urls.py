from django.urls import path
from .views import Flux, Ticket, Ticket_review
urlpatterns = [
    path("flux/", Flux.as_view(), name="flux"),
    path("ticket/", Ticket.as_view(), name="ticket"),
    path("ticket_review/", Ticket_review.as_view(), name="ticket_review"),

]
