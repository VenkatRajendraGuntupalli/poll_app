from django.forms import ModelForm
from .models import UserPoll

class UserPollForm(ModelForm):
    class Meta:
        model = UserPoll
        fields = ['query_text', 'choice_x', 'choice_y', 'choice_z']