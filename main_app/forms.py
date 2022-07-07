from django.forms import ModelForm
from .models import LipSyncs

class LipSyncsForm(ModelForm):
  class Meta:
    model = LipSyncs
    fields = ['season', 'episode', 'song', 'vs']