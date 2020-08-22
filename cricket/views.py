from django.shortcuts import render
from .models import Match, Team, Player, Point
from django.db.models import Q
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Count

# Create your views here.


def team_list(request):
    team_list = Team.objects.all()
    paginator=Paginator(team_list, 10)
    page_number=request.GET.get('page')
    try:
        team_list=paginator.page(page_number)
    except PageNotAnInteger:
        team_list=paginator.page(1)
    except EmptyPage:
        team_list=paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'team_list':team_list})


def team_detail(request, pk):
    team_obj = Team.objects.get(id=pk)
    player_obj = Player.objects.filter(team = team_obj)
    return render(request, 'team_detail.html', {'player_obj':player_obj,'team':team_obj})

def fixture(request):
    match_obj = Match.objects.all().order_by('created_at')
    print(match_obj)
    fixture = []
    for match in match_obj:
        fixture.append(match)
    print(fixture)
    return render(request, 'fixture.html', {'match_obj':fixture})  

def points_table(request):
    points_obj = Point.objects.all().order_by('-won')
    print(points_obj)
    points = []
    for point in points_obj:
        points.append(point)
    print(points)
    return render(request, 'points.html', {'points':points})  