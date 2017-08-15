from django import forms

from .models import Business, Employment


class CreateBusinessForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super(CreateBusinessForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'create-input'

    def save(self, commit=True, **kwargs):
        business = super(CreateBusinessForm, self).save(commit=False)  # model instance
        if commit:
            business.save()
            employment = Employment.objects.create(business=business, employee=kwargs['user'], is_admin=True)
            employment.save()
        return business

