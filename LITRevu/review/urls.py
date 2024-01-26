from django.urls import path
from .views import (
    TicketListView,
    TicketCreateView,
    TicketDetailView,
    TicketUpdateView,
    TicketDeleteView,
    TicketReviewCreateView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView,
)

urlpatterns = [
    path("flux/", TicketListView.as_view(), name="flux"),
]

# Ticket
urlpatterns += (
    path("ticket/create/", TicketCreateView.as_view(), name="ticket"),          # C
    path("ticket/<int:pk>/", TicketDetailView.as_view(), name="ticket"),        # R
    path("ticket/update/<int:pk>/", TicketUpdateView.as_view(), name="ticket"),  # U
    path("ticket/delete/<int:pk>/", TicketDeleteView.as_view(), name="ticket"),  # D
)
# create and review a ticket at the same time
urlpatterns += (
    path("ticket_review/create/",
         TicketReviewCreateView.as_view(), name="ticket_review"),

)
# Review
urlpatterns += (
    path("review/create/", ReviewCreateView.as_view(), name="review"),
    path("review/update/<int:pk>/", ReviewUpdateView.as_view(), name="review"),
    path("review/delete/<int:pk>/", ReviewDeleteView.as_view(), name="review"),
)
