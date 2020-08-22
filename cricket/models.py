from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    captain = models.CharField(max_length=100, blank=True, null=True)
    vice_captain = models.CharField(max_length=100, blank=True, null=True)
    coach = models.CharField(max_length=100, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to="team_logo")
    club = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField()
    dob = models.DateField()
    total_run = models.PositiveIntegerField(default=0)
    total_wicket = models.PositiveIntegerField(default=0)
    total_match = models.PositiveIntegerField(default=0)
    highest_score = models.PositiveIntegerField(default=0)
    fifties = models.PositiveIntegerField(default=0)
    hundreds = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="player")
    jursey_number = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name        

class Match(models.Model):
    match_number = models.PositiveIntegerField(default=0)
    match_type = models.CharField(max_length=100, blank=True)
    team1 = models.ForeignKey(Team,  related_name='teamone', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team,  related_name='teamtwo', on_delete=models.CASCADE)
    winner = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=False)
    description = models.TextField(blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
       
    def __str__(self):
        return self.winner      
       

class Point(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    play = models.PositiveIntegerField(default=0)
    won = models.PositiveIntegerField(default=0)
    lost = models.PositiveIntegerField(default=0)
    tie  = models.PositiveIntegerField(default=0)
    total_points = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.team.name   
   