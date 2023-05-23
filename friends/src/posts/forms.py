from django import forms

class postEditForm(forms.Form):
    content = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(
            attrs={
                'Placeholder': 'Explain your problem...',
                'class': 'form-control mb-2',
                'id': 'content',
                'style': 'height: 180px;'
            }
        )
    )
    def __init__(self, post, *args, **kwargs):
        super(postEditForm, self).__init__(*args, **kwargs)
        self.initial['content'] = post.content

    def clean(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if content is None or len(content) == 0:
            raise forms.ValidationError("Content can't be blank.")
        return super(postEditForm, self).clean(*args, **kwargs)


class postForm(forms.Form):
    content = forms.CharField(
        required=False,
        label='',
        widget=forms.Textarea(
            attrs={
                'Placeholder': 'Explain your problem...',
                'class': 'form-control mb-2',
                'id': 'content',
                'style': 'height: 180px;'
            }
        )
    )

    photo1 = forms.ImageField(label='', required=False)
    photo2 = forms.ImageField(label='', required=False)
    photo3 = forms.ImageField(label='', required=False)
    photo1.widget.attrs['id'] = 'inPhoto1'
    photo1.widget.attrs['style'] = 'display:none;'

    photo2.widget.attrs['id'] = 'inPhoto2'
    photo2.widget.attrs['style'] = 'display:none;'

    photo3.widget.attrs['id'] = 'inPhoto3'
    photo3.widget.attrs['style'] = 'display:none;'
    def clean(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if content is None or len(content) == 0:
            raise forms.ValidationError("Write something to post.")
        return super(postForm, self).clean(*args, **kwargs)
