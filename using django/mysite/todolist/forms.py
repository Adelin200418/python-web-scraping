from django import forms


class  TodoListForm(forms.Form):
    text= forms.CharField(max_length=45,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'Enter to do e.g wash dishes','aria-label':'Todo','aris-describeby':'add-btn'}
        ))
