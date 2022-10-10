from django import forms
from django.core.validators import FileExtensionValidator

class UploadForm(forms.Form):
    file = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes',
        validators=[FileExtensionValidator(allowed_extensions=['xlsx', 'xls'])]
    )
    