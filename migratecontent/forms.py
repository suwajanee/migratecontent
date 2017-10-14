from django import forms

class PageExportForm(forms.Form):

	title_tag = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'title_tag'
			}
		),
		required=True
	)

	TITLE_CHOICES = (
		('id', 'id'),
		('class', 'class'),
	)

	title_class_type = forms.ChoiceField(
		choices=TITLE_CHOICES,
		required=True
	)

	title_class = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'title_class'
			}
		),
		required=True
	)

	content_tag = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'content_tag'
			}
		),
		required=True
	)

	CONTENT_CHOICES = (
		('id', 'id'),
		('class', 'class'),
	)

	content_class_type = forms.ChoiceField(
		choices=CONTENT_CHOICES,
		required=True
	)

	content_class = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'content_class'
			}
		),
		required=True
	)

	content_order = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'content_order'
			}
		),
		initial=1
	)

	upload_file = forms.FileField()

	SIDEBAR_CHOICES = (
		('default', 'Default'),
		('left', 'Left'),
		('right', 'Right'),
		('full-width', 'Full-Width')
	)

	page_sidebar = forms.ChoiceField(
		choices=SIDEBAR_CHOICES,
		required=True
	)


class PageImportForm(forms.Form):

	host_url = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'host_url'
			}
		),
		required=True
	)

	upload_file = forms.FileField()

	id_field = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'id_field'
			}
		),
		required=True
	)

	password_field = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'id': 'password_field'
			}
		),
		required=True
	)

class DecomposeForm(forms.Form):

	decompose_tag = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'decompose_tag'
			}
		),
		required=False
	)

	CONTENT_CHOICES = (
		('id', 'id'),
		('class', 'class'),
	)

	decompose_type = forms.ChoiceField(
		choices=CONTENT_CHOICES,
		required=True
	)

	decompose_class = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'decompose_class'
			}
		),
		required=False
	)

	upload_file = forms.FileField()

	decompose_order = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'decompose_order'
			}
		),
		initial=1
	)

class BlogExportForm(forms.Form):

	title_tag = forms.CharField(
		widget=forms.TextInput(
			attrs={
			'id': 'title'
			}
		),
		required=True
	)

	TITLE_CHOICES = (
		('id', 'id'),
		('class', 'class'),
	)

	title_class_type = forms.ChoiceField(
		choices=TITLE_CHOICES,
		required=True
	)

	title_class = forms.CharField(
		widget=forms.TextInput(
			attrs={
			'id': 'title_class'
			}
		),
		required=True
	)

	date_tag = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'date_tag'
			}
		),
	)

	DATE_CHOICES = (
		('id', 'id'),
		('class', 'class'),
	)

	date_class_type = forms.ChoiceField(
		choices=DATE_CHOICES
	)

	date_class = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'date_class'
			}
		),
	)

	date_remove_text = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'date_remove_text'
			}
		),
	)

	content_tag = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'content_tag'
			}
		),
		required=True
	)

	CONTENT_CHOICES = (
		('id', 'id'),
		('class', 'class'),
	)

	content_class_type = forms.ChoiceField(
		choices=CONTENT_CHOICES,
		required=True
	)

	content_class = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'content_class'
			}
		),
		required=True
	)

	content_order = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'content_order'
			}
		),
		initial=1
	)

	upload_file = forms.FileField()

class BlogImportForm(forms.Form):

	host_url = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'host_url'
			}
		),
		required=True
	)

	upload_file = forms.FileField()

	id_field = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'id_field'
			}
		),
		required=True
	)

	password_field = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'id': 'password_field'
			}
		),
		required=True
	)	

	upload_file = forms.FileField()