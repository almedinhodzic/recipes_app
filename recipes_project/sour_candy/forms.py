from django import forms

from .models import Recipe, Profile


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ('creator',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({"class": "form-select"})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
