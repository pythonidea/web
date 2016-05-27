from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User


class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()
    def save(self):
        return Answer.objects.create(
            text=self.cleaned_data['text'],
            question_id=self.cleaned_data['question'],
            author=getattr(self, '_user', None),
        )