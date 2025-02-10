from django.db import models

class UserPoll(models.Model):
    query_text = models.TextField()
    choice_x = models.CharField(max_length=30)
    choice_y = models.CharField(max_length=30)
    choice_z = models.CharField(max_length=30)
    votes_choice_x = models.IntegerField(default=0)
    votes_choice_y = models.IntegerField(default=0)
    votes_choice_z = models.IntegerField(default=0)

    def total_votes(self):
        return self.votes_choice_x + self.votes_choice_y + self.votes_choice_z
