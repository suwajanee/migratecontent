import base64
import csv
import json
import os

from django.shortcuts import render
from django.views.generic import TemplateView

import requests
import urllib
from bs4 import BeautifulSoup

from ..forms import PageImportForm


class PageImportView(TemplateView):
	template_name = 'page_import.html'

	def get(self, request):
		form = PageImportForm()
		return render(
			request, self.template_name, {'form': form})

	def create_page(self, headers, host_url, data):
		
		#prevent last / slug of host_url
		if host_url[-1:] == '/':
			host_url = host_url[:-1]

		url = host_url + '/wp-json/wp/v2/pages'
		last_url_source =  data['page_source']

		#get last slug of last_url 
		if last_url_source[-1:] == '/':
			last_url = last_url_source[:-1].split('/')[-1]
		else:
			last_url = last_url_source.split('/')[-1]

		post_data = {
			'status': 'publish',
			'title': data['title'],
			'content': data['content'],
			'slug': last_url
		}
		
		r = requests.post(url, headers=headers, data=post_data)
		response = json.loads(r.content)
		page_url = response['guid']['rendered']
		return page_url

	def gather_image(self, json_data):
		image_list_outer = []

		for data in json_data:
			soup = BeautifulSoup(data['content'], 'html.parser')
			page_source = data['page_source']

			for img_srcs in soup.findAll('img'):
				img_src = img_srcs.get('src')

				image_list_inner = []

				if "www" in img_src: 
					old_image = img_src
					image_list_inner.append(old_image)

					new_image = img_src 
					image_list_inner.append(new_image)

				elif ".." in img_src:
					old_image = img_src
					image_list_inner.append(old_image)
					
					new_image = page_source + old_image.split('..')[1]
					image_list_inner.append(new_image)

				else:
					old_image = img_src
					image_list_inner.append(old_image)
					
					new_image = page_source + '/' + old_image
					image_list_inner.append(new_image)

				image_list_outer.append(image_list_inner)

		return image_list_outer

	def clean_img_url(self, img_url):
		if '/image_' in img_url:
			img_url = img_url.split('/image_')[0]
		return img_url

	def upload_image(self, headers, host_url, images):
		img_dict = {}
		url = host_url + '/wp-json/wp/v2/media'
		for img_url in images:
			key = img_url[0]
			download_url = self.clean_img_url(img_url[1])
			if not img_dict.has_key(key):
				img_name = download_url.split('/')[-1]
				if '.' not in img_name:
					img_name = img_name + '.jpg'
				img_path = 'media/' + img_name
				urllib.urlretrieve(download_url, img_path)
				with open(img_path) as img:
					files = {'file': img}
					img_data = {
						'title':img_name,
						'status':'publish'
					}
					r = requests.post(url, data=img_data, headers=headers, files=files)
					img_response = json.loads(r.content)
					img_dict[key] = img_response['guid']['rendered']
		return img_dict

	def post(self, request):
		json_file = request.FILES['upload_file']
		host_url = request.POST['host_url']
		user_id = request.POST['id_field']
		user_password = request.POST['password_field']

		auth = base64.b64encode(user_id + ':' + user_password)
		headers = {'Authorization': 'Basic ' + auth}

		json_file = json_file.read()
		json_data = json.loads(json_file)

		image_list = self.gather_image(json_data)
		img_dict = self.upload_image(headers, host_url, image_list)
		for key,value in img_dict.iteritems():
			json_file = json_file.replace(key,value)

		json_data = json.loads(json_file)
		pages = []
		for data in json_data:
			page_url = self.create_page(headers, host_url, data)
			pages.append(
				{
					'url': page_url,
					'title': data['title']
				})

		return render(
			request, 'result.html', {'data': pages, 'type': 'Page'})
