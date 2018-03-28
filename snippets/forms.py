from django import forms 


class Snippetform(forms.Form)
	title  = forms.CharField(label='Title' ,max_length=30)
	content = fomrs.TextField(label='Content')

