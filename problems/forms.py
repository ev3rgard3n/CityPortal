from django import forms
from .models import Problems, Categories

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

class AdminProblemForm(forms.ModelForm):
    image_resolved_upload = forms.ImageField(required=False, label="Загрузить изображение решенной проблемы")  # Поле для загрузки изображения

    class Meta:
        model = Problems
        fields = ['status']  # Только редактируемые поля

    def save(self, commit=True):
        problem = super().save(commit=False)

        # Если загружено новое изображение для `image_resolved`
        if self.cleaned_data.get('image_resolved_upload'):
            uploaded_image = self.cleaned_data['image_resolved_upload']
            problem.image_resolved = uploaded_image.read()  # Сохраняем изображение в поле BinaryField

        if commit:
            problem.save()
        return problem
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'slug']
