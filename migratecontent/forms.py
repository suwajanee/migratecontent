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
		('', '-'),
		('id', 'id'),
		('class', 'class'),
	)

	title_class_type = forms.ChoiceField(
		choices=TITLE_CHOICES,
		required=False
	)

	title_class = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'title_class'
			}
		),
		required=False
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

	upload_file = forms.FileField()


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
		('itemprop', 'itemprop'),
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
		('', '-'),
		('id', 'id'),
		('class', 'class'),
		('itemprop', 'itemprop'),
	)
	title_class_type = forms.ChoiceField(
		choices=TITLE_CHOICES,
		required=False
	)

	title_class = forms.CharField(
		widget=forms.TextInput(
			attrs={
			'id': 'title_class'
			}
		),
		required=False
	)

	date_tag = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'date_tag'
			}
		),
		required=False
	)

	DATE_CHOICES = (
		('', '-'),
		('id', 'id'),
		('class', 'class'),
		('itemprop', 'itemprop'),
	)
	date_class_type = forms.ChoiceField(
		choices=DATE_CHOICES,
		required=False
	)

	date_class = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'date_class'
			}
		),
		required=False
	)

	date_remove_text = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'date_remove_text'
			}
		),
		required=False
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
		('itemprop', 'itemprop'),
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