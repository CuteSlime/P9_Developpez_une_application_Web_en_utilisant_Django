from django.contrib import admin

from review.models import Ticket, Review, UserFollows


class TicketAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('title', 'user', 'time_created')


class ReviewAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('headline', 'ticket', 'rating', 'user', 'time_created')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserFollows)
