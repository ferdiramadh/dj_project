from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
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
	'css_app':'blog/css/style.css',
	}
	return render(request,'blog/index.html', context)

def cerita(request):
	context = {
	'judul' : 'INi cerita',
	'kontributor' : 'sapa_ya',
	}
	return render(request,'blog/index.html', context)

def news(request):
	context = {
	'judul' : 'news berita',
	'kontributor' : 'mawang',
	}
	return render(request,'blog/index.html', context)

def recent(request):
	return HttpResponse("Ini Recent")