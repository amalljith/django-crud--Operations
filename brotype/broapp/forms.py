from .models import De
from django.forms import ModelForm

class DeForm(ModelForm):
    class Meta:
        model = De
        fields = "__all__"
