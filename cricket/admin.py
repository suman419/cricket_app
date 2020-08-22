from django.contrib import admin
from .models import Match, Team, Player, Point
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name','club','created_at','udated_at']
admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Point)