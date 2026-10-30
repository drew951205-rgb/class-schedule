from django import forms
from .models import Course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'teacher', 'weekday', 'start', 'end', 'classroom']
    def clean(self):
        data = super().clean()
        start, end, day = data.get('start'), data.get('end'), data.get('weekday')
        if start and end and start > end:
            raise forms.ValidationError('結束節次不能早於開始節次。')
        if start and end and day and start <= end:
            overlaps = Course.objects.filter(weekday=day, start__lte=end, end__gte=start).exclude(pk=self.instance.pk)
            if overlaps.exists():
                raise forms.ValidationError('這段節次已有其他課程，請調整時間。')
        return data
