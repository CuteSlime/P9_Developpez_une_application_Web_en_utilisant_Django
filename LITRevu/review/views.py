from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Ticket, Review, UserFollows
from accounts.models import CustomUser
from .forms import RatingForm, FollowUserForm


# Flux
class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = "review/flux.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_followed = UserFollows.objects.filter(
            user=self.request.user).values_list('followed_user', flat=True)
        ticket_author = Ticket.objects.filter(user=self.request.user)

        tickets = [{'content': ticket, 'timestamp': ticket.time_created, 'reviewed': Review.objects.filter(user=self.request.user, ticket=ticket).exists()}
                   for ticket in Ticket.objects.filter(Q(user__in=user_followed) |
                                                       Q(user=self.request.user))]
        reviews = [{'content': review, 'timestamp': review.time_created}
                   for review in Review.objects.filter(Q(user__in=user_followed) |
                                                       Q(user=self.request.user) |
                                                       Q(ticket__in=ticket_author))]

        flux = sorted(tickets + reviews,
                      key=lambda item: item['timestamp'], reverse=True)

        context['flux'] = flux
        # context['review'] = Review.objects.all()
        return context


# Post
class PostListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = "review/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tickets = [{'content': ticket, 'timestamp': ticket.time_created, 'reviewed': Review.objects.filter(user=self.request.user, ticket=ticket).exists()}
                   for ticket in Ticket.objects.filter(user=self.request.user)]
        reviews = [{'content': review, 'timestamp': review.time_created}
                   for review in Review.objects.filter(user=self.request.user)]

        posts = sorted(tickets + reviews,
                       key=lambda item: item['timestamp'], reverse=True)

        context['posts'] = posts
        return context


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


class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = "review/ticket.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviewed'] = Review.objects.filter(
            user=self.request.user, ticket=self.object).exists()
        return context


class TicketUpdateView(UserPassesTestMixin, UpdateView):
    raise_exception = True
    model = Ticket
    success_url = reverse_lazy("flux")
    template_name = "review/ticket_update.html"
    fields = (
        "title",
        "description",
        "image",
    )

    def test_func(self):
        ticket = self.get_object()
        return self.request.user == ticket.user
    raise_exception = True


class TicketDeleteView(UserPassesTestMixin, DeleteView):
    raise_exception = True
    model = Ticket
    template_name = "review/ticket_delete.html"
    success_url = reverse_lazy("flux")

    def test_func(self):
        ticket = self.get_object()
        return self.request.user == ticket.user


# create and review a ticket at the same time
class TicketReviewCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = "review/ticket_review_new.html"
    fields = ("title", "description", "image",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['review'] = RatingForm(self.request.POST)
        else:
            context['review'] = RatingForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        review = context['review']
        form.instance.user = self.request.user
        self.object = form.save()
        if review.is_valid():
            review.instance.ticket = self.object
            review.instance.user = self.request.user
            review.save()
        else:
            print(review.errors)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('flux')
# review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "review/review_new.html"
    form_class = RatingForm

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
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ticket', kwargs={'pk': self.object.ticket.pk})


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = "review/flux.html"


class ReviewUpdateView(UserPassesTestMixin, UpdateView):
    raise_exception = True
    model = Review
    form_class = RatingForm
    template_name = "review/review_update.html"

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user

    def get_success_url(self):
        return reverse_lazy('ticket', kwargs={'pk': self.object.ticket.pk})


class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    raise_exception = True
    model = Review
    template_name = "review/review_delete.html"

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user

    def get_success_url(self):
        return reverse_lazy('ticket', kwargs={'pk': self.object.ticket.pk})


# follower and followed
class UserFollowsListView(LoginRequiredMixin, ListView):
    model = UserFollows
    template_name = 'review/follow.html'
    context_object_name = 'user_follows'

    def get_queryset(self):
        return UserFollows.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = getattr(
            self, 'form', FollowUserForm(user=self.request.user))

        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        username = request.POST.get('username')
        self.form = FollowUserForm(request.POST, user=request.user)
        if action == 'follow' and self.form.is_valid():
            user_to_follow = CustomUser.objects.get(username=username)
            UserFollows.objects.get_or_create(
                user=request.user, followed_user=user_to_follow)
        elif action == 'unfollow':
            user_to_unfollow = CustomUser.objects.get(username=username)
            UserFollows.objects.filter(
                user=request.user, followed_user=user_to_unfollow).delete()
        return self.get(request, *args, **kwargs)
