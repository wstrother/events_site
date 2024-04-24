from django import forms

def getVoteForm(choice_set):
    choice_set = [(c.id, c.choice_text) for c in choice_set]
    
    class VoteForm(forms.Form):
        template_name = 'polls/components/forms/vote_form.html'
        choices = forms.ChoiceField(choices=choice_set, required=True, widget=forms.RadioSelect)

    return VoteForm
