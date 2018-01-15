import csv
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import requests
import urllib2
from bs4 import BeautifulSoup, NavigableString

from ..forms import DecomposeForm


class DecomposeView(TemplateView):
	template_name = 'decompose.html'

	def get(self, request):
		form = DecomposeForm()
		return render(
			request, self.template_name, {'form': form})

	def post(self, request):
		json_file = request.FILES['upload_file']
		tag_data = str(request.POST['decompose_tag'])
		class_data = str(request.POST['decompose_class'])
		decompose_type = str(request.POST['decompose_type'])

		json_data = json.loads(json_file.read())
		page_json = []

		decompose_order_list = []
		for data in json_data:
			soup = BeautifulSoup(data['content'], 'html.parser')

			try:
				soup.find(tag_data,{decompose_type: class_data}).decompose()
			except:
				pass

			data['content'] = str(soup)
			page_json.append(data)

		data = json.dumps(page_json)
		response = HttpResponse(content=data)
		response['Content-Type'] = 'application/json'
		response['Content-Disposition'] = 'attachment; filename="page_content.json"'
		return response
