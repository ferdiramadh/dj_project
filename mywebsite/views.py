from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context = {
		'judul' : 'Test Template Variable',
		'kontributor' : 'saya',
		'nav' : 	[
				['/', 'Home'],
				['/blog', 'Blog'],
				['/about', 'About'],
				['blog/cerita', 'Cerita']
			],
		'banner':'blog/img/images.jpeg',
		'banner_home':'img/web-design-banner-png-4.png',
		}
	return render(request, 'index.html', context)

def about(request):
	return render(request, 'about.html')