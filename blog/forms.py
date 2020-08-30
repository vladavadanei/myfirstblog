from django import forms
from .models import Post
from .models import Cv

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text')
		
class CvForm(forms.ModelForm):

	class Meta:
		model = Cv
		fields = ('title', 'text', 'name', 'address', 'contact', 'Introduction', 'Experience', 'Qualifications')