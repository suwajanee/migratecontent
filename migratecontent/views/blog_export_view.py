import csv
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import requests
import urllib2
from bs4 import BeautifulSoup, NavigableString

from ..forms import BlogExportForm


class BlogExportView(TemplateView):
	template_name = 'blog_export.html'

	def get(self, request):
		form = BlogExportForm()
		return render(
			request, self.template_name, {'form': form})

	def clean_date_text(self, date_data, date_remove_text):
		date = date_data.replace(date_remove_text,'')
		date = date.strip(' \t\r\n')
		return date

	def post(self, request):
		csv_file = request.FILES['upload_file']

		title_tag = request.POST['title_tag']
		title_class_type = request.POST['title_class_type']
		title_class = request.POST['title_class']
		date_tag = request.POST['date_tag']
		date_class_type = request.POST['date_class_type']
		date_class = request.POST['date_class']
		date_remove_text = request.POST['date_remove_text']
		content_tag = request.POST['content_tag']
		content_class_type = request.POST['content_class_type']
		content_class = request.POST['content_class']

		post_json = []
		reader = csv.reader(csv_file, delimiter=',')
		for row in reader:
			website_url = row[0]

			html_page = urllib2.urlopen(website_url)
			soup = BeautifulSoup(html_page, "html.parser")


			title = ''
			for titles in soup.find(title_tag, {title_class_type:title_class}):
				try:
					title = titles.text
				except:
					title = str(titles)


			date = ''
			for dates in soup.find(date_tag, {date_class_type:date_class}):
				date_data = str(dates)
				date = self.clean_date_text(date_data, date_remove_text)

			content = ''
			for contents in soup.find(content_tag, {content_class_type:content_class}):
				content += str(contents)

			image = ''
			try:
				soup = BeautifulSoup(content, "html.parser")
				image = soup.find('img').get('src')
			except:
				pass

			data_json = {
					'title': title,
					'date': date,
					'content': content,
					'image': image,
					'page_source': website_url,
				}

			post_json.append(data_json)

		data = json.dumps(post_json)
		response = HttpResponse(content=data)
		response['Content-Type'] = 'application/json'
		response['Content-Disposition'] = 'attachment; filename="post_content.json"'
		return response
		