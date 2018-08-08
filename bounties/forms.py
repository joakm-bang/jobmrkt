from django import forms
#from django.contrib.auth.models import User
from bounties.models import Bounty



class NewBountyForm(forms.Form):
    
    # TODO: Add a dropdown list of companies registered to this user
    
    title = forms.CharField(widget=forms.TextInput(attrs={'id': 'bounty_title', 'class': 'textbox'}), 
                            label='Title', max_length=255, required = True, 
                            error_messages={'required': 'You must enter a title for your bounty.'})
    description = forms.CharField(widget=forms.TextInput(attrs={'id': 'bounty_description', 'class':'textbox'}), 
                                  label='Description', max_length=4000, required = True, 
                                  error_messages={'required': "You must enter a description of the role you want to fill."})

    size = forms.FloatField(required=False, max_value=10**10, min_value=0, label='Bounty size ($)', 
                            widget=forms.NumberInput(attrs={'id': 'bounty_size', 'class':'textbox', 'step':10}),
                            error_messages={'max_value': "The bounty must be smaller.",
                                            'min_value': "The bounty must be larger than 0. You may leave it blank if you wish to decide on the bounty size later.",})
    
