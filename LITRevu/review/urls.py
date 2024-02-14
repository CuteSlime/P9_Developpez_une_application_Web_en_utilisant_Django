from django.urls import path

from .views import (
    TicketListView,
    PostListView,
    TicketCreateView,
    TicketDetailView,
    TicketUpdateView,
    TicketDeleteView,
    TicketReviewCreateView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView,
    UserFollowsListView,
)

urlpatterns = [
    path("flux/", TicketListView.as_view(), name="flux"),
    path("post/", PostListView.as_view(), name="post"),
]

# Ticket
urlpatterns += (
    path("ticket/new/", TicketCreateView.as_view(),
         name="ticket_create"),                                     # C
    path("ticket/<int:pk>/", TicketDetailView.as_view(),
         name="ticket"),                                            # R
    path("ticket/update/<int:pk>/", TicketUpdateView.as_view(),
         name="ticket_update"),                                     # U
    path("ticket/delete/<int:pk>/", TicketDeleteView.as_view(),
         name="ticket_delete"),                                     # D
)
# create and review a ticket at the same time
urlpatterns += (
    path("ticket_review/new/",
         TicketReviewCreateView.as_view(), name="ticket_review_create"),

)
# Review
urlpatterns += (
    path("review/new/<int:ticket_id>",
         ReviewCreateView.as_view(), name="review_create"),
    path("review/update/<int:pk>/",
         ReviewUpdateView.as_view(), name="review_update"),
    path("review/delete/<int:pk>/",
         ReviewDeleteView.as_view(), name="review_delete"),
)

# Follow
urlpatterns += (
    path("follow/",
         UserFollowsListView.as_view(), name="follow"),

)
