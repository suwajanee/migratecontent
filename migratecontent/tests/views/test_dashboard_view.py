from django.core.urlresolvers import reverse
from django.test import TestCase

class DashboardViewTest(TestCase):

	def setUp(self):
		self.dashboard_url = reverse('dashboard')

	def test_dashboard_view_should_render_correct_elements(self):
		response = self.client.get(self.dashboard_url)

		page_export_url = reverse('page_export')
		expected = '<a href="{0}">'.format(page_export_url)
		self.assertContains(response, expected, status_code=200)

		page_import_url = reverse('page_import')
		expected = '<a href="{0}">'.format(page_import_url)
		self.assertContains(response, expected, status_code=200)

		decompose_url = reverse('decompose')
		expected = '<a href="{0}">'.format(decompose_url)
		self.assertContains(response, expected, status_code=200)

		blog_import_url = reverse('blog_import')
		expected = '<a href="{0}">'.format(decompose_url)
		self.assertContains(response, expected, status_code=200)

		blog_export_url = reverse('blog_export')
		expected = '<a href="{0}">'.format(decompose_url)
		self.assertContains(response, expected, status_code=200)