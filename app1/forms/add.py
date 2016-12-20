from django import forms

class AddForm(forms.Form):
	name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	status = forms.BooleanField(required=False)
