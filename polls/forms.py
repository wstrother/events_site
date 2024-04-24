from django import forms

def getVoteForm(choices):
    choices = [(c.id, c.choice_text) for c in choices]
    class VoteForm(forms.Form):
        choice = forms.ChoiceField(choices=choices, required=True, widget=forms.RadioSelect)
    
    return VoteForm
