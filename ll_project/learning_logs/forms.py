from django import forms

from .models import Entry, Topic


class TopicForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop("request_user", None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""}

    def clean_text(self):
        text = self.cleaned_data["text"].strip()

        # Check if empty
        if not text:
            raise forms.ValidationError("Topic cannot be empty.")

        if self.instance.pk:
            owner = self.instance.owner
        else:
            owner = self.request_user

        duplicate_exists = Topic.objects.filter(
            owner=owner,
            text__iexact=text,
        ).exists()

        if duplicate_exists:
            raise forms.ValidationError("You already have this topic.")

        return text


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}

    def clean_text(self):
        text = self.cleaned_data["text"].strip()
        if not text:
            raise forms.ValidationError("Entry cannot be empty.")

        return text
