from django import forms
from django.core.validators import FileExtensionValidator
from report.models import Door

class UploadForm(forms.Form):
    file = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes',
        validators=[FileExtensionValidator(allowed_extensions=['xlsx'])]
    )

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class SearchForm(forms.Form):
    door_id = forms.ChoiceField(choices=Door.get_options())
    record_date = forms.DateField(widget=DatePickerInput)
