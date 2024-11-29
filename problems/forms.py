from django import forms
from .models import Problems

class ProblemForm(forms.ModelForm):
    # Добавляем поля загрузки изображений
    image = forms.ImageField(required=False, label="Изображение проблемы")
    image_resolved = forms.ImageField(required=False, label="Изображение решенной проблемы")

    class Meta:
        model = Problems
        exclude = ['image_resolved', 'user', 'status']  # Исключаем BinaryField

    def save(self, commit=True):
        problem = super().save(commit=False)

        # Обрабатываем изображение для хранения в BinaryField
        if self.cleaned_data.get('image'):
            problem.image = self.cleaned_data['image'].read()
        if self.cleaned_data.get('image_resolved'):
            problem.image_resolved = self.cleaned_data['image_resolved'].read()

        if commit:
            problem.save()
        return problem
