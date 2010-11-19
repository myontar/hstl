# To change this template, choose Tools | Templates
# and open the template in the editor.
from django import forms
from hmain.models import *
from ragendja.auth.models import UserTraits
from ragendja.forms import FormWithSets, FormSetField

__author__="John"
__date__ ="$16.Kas.2010 15:18:26$"

class LanguagesForm(forms.ModelForm):
    name = forms.CharField(required=True, label='Name')

    class Meta:
        model = Languages

