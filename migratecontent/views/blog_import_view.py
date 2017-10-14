import base64
import csv
import json

from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import requests
import urllib
import urllib2
from bs4 import BeautifulSoup, NavigableString

from ..forms import BlogImportForm


class BlogImportView(TemplateView):
	template_name = 'blog_import.html'

	def get(self, request):
		form = BlogImportForm()
		return render(
			request, self.template_name, {'form': form})

	def create_post(self, headers, host_url, data, img_id):
		#check / behind url
		if host_url[-1:] == '/':
			host_url = host_url[:-1]

		url = host_url + '/wp-json/wp/v2/posts'
		post_date = datetime.strptime(data['date'], '%B %d, %Y')


		post_data = {
			'status': 'publish',
			'title': data['title'],
			'content': data['content'],
			'date': post_date,
			'categories': data['categories'],
			'tags': data['tags'],
			'featured_media': img_id
		}

		r = requests.post(url, headers=headers, data=post_data)
		response = json.loads(r.content)
		post_url = response['guid']['rendered']
		return post_url

	def clean_img_url(self, img_url):
		if '/image_' in img_url:
			img_url = img_url.split('/image_')[0]
		return img_url

	def gather_image(self, data):
		image_list_outer = []

		# for data in json_data:
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

	def upload_image(self, headers, host_url, images, feature_img):
		img_dict = {}
		img_id = ''
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
						'title': img_name,
						'status': 'publish'
					}

					r = requests.post(url, data=img_data, headers=headers, files=files)
					img_response = json.loads(r.content)
					img_dict[key] = img_response['guid']['rendered']
					# print img_dict[key].split("/")[-1]
					if feature_img == key:
						img_id = img_response['id']

					# img_id.append(img_response['id'])

		return img_dict, img_id

	def fix_link(self, data):
		soup = BeautifulSoup(data['content'], 'html.parser')
		page_source = data['page_source']

		for link in soup.findAll('a'):
			old_url = link.get('href')
			old_url_split = old_url.split('/',3)
			try:
				if old_url_split[2] in page_source:
					new_url = '/' + old_url_split[3]
					data['content'] = data['content'].replace(old_url, new_url)
			except:
				data['content']
		return data['content']


	def post(self, request):
		json_file = request.FILES['upload_file']

		host_url = request.POST['host_url']
		user_id = request.POST['id_field']
		user_password = request.POST['password_field']

		if host_url[-1:] == '/':
			host_url = host_url[:-1]

		auth = base64.b64encode(user_id + ':' + user_password)
		headers = {'Authorization': 'Basic ' + auth}

		json_file = json_file.read()
		json_data = json.loads(json_file)

		posts = []
		for data in json_data:
			image_list = self.gather_image(data)
			img_dict, img_id = self.upload_image(headers, host_url, image_list, data['image'])

			if data['image']:
				img_id = img_id
			else:
				img_id = 0

			for key,value in img_dict.iteritems():
				value = value.replace(host_url, '')
				data['content'] = data['content'].replace(key, value)

			data['content'] = self.fix_link(data)

			post_url = self.create_post(headers, host_url, data, img_id)

			posts.append(
				{
					'url': post_url,
					'title': data['title']
				})
		return render(
			request, 'result.html', {'datas': posts, 'type': 'Post'})
