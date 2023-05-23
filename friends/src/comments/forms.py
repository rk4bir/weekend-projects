from django import forms


class commentEditForm(forms.Form):
    content = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(
            attrs={
                'Placeholder': 'Comment.',
                'class': 'form-control mb-2',
                'id': 'content',
                'style': 'height: 180px;'
            }
        )
    )
    def __init__(self, comment, *args, **kwargs):
        super(commentEditForm, self).__init__(*args, **kwargs)
        self.initial['content'] = comment.content

    def clean(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if content is None or len(content) == 0:
            raise forms.ValidationError("Content can't be blank.")
        return super(commentEditForm, self).clean(*args, **kwargs)

