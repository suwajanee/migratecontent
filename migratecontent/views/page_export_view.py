import csv
import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import urllib2
from bs4 import BeautifulSoup, NavigableString

from ..forms import PageExportForm


class PageExportView(TemplateView):
	template_name = 'page_export.html'

	def get(self, request):
		form = PageExportForm()
		return render(
			request, self.template_name, {'form': form})

	def post(self, request):
		csv_file = request.FILES['upload_file']

		title_tag = request.POST['title_tag']
		title_class_type = request.POST['title_class_type']
		title_class = request.POST['title_class']
		content_tag = request.POST['content_tag']
		content_class_type = request.POST['content_class_type']
		content_class = request.POST['content_class']	

		page_json = [] 
		reader = csv.reader(csv_file, delimiter=',')
		for row in reader:
			website_url = row[0]

			html_page = urllib2.urlopen(website_url)
			soup = BeautifulSoup(html_page, "html.parser" )
			
			try:
				for titles in soup.find(title_tag, {title_class_type:title_class}):
					try:
						title = titles.text
					except:
						title = str(titles)
			except:
				title = ''
			
			content = ''
			for contents in soup.find(content_tag, {content_class_type:content_class}):
				content += str(contents)

			data_json = {
					'title': title,
					'content': content,
					'page_source' : website_url
				}

			page_json.append(data_json)

		data = json.dumps(page_json)
		response = HttpResponse(content=data)
		response['Content-Type'] = 'application/json'
		response['Content-Disposition'] = 'attachment; filename="page_content.json"'
		return response
		