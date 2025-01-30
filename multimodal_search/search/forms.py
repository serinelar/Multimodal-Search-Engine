from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=255, required=False)
    data_type = forms.ChoiceField(
        label='Filter by Type',
        choices=[
            ('all', 'All'),
            ('text_content', 'Text'),
            ('image', 'Image'),
            ('audio', 'Audio'),
            ('video', 'Video'),
        ],
        required=False,
    )