import os

from django.core.urlresolvers import reverse
from django.test import TestCase


class PageExportViewTest(TestCase):

	def setUp(self):
		self.page_export_url = reverse('page_export')

	def test_post_page_export_view_should_return_json_file(self):
		csv_file_path = os.path.dirname(os.path.abspath(__file__))
		csv_file_path += '/files/test_page_export.csv'
		csv_file = open(csv_file_path, 'r')
		
		data = {
			'title_tag': 'div',
			'title_class_type': 'class',
			'title_class': 'content',
			'content_tag': 'div',
			'content_class_type': 'id',
			'content_class': 'left-column',
			'content_order': '1',
			'page_sidebar': 'default',
			'upload_file': csv_file
		}

		response = self.client.post(self.page_export_url, data)
		print response

