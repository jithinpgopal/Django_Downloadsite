from django.shortcuts import render
from .utils import image_download

# Create your views here.


def download(request):
	return render(request, 'app_igdl/download.html')

def image(request):
	# print ("Printing :" + request.POST.get("q"))
	url1 = str(request.POST.get("q"))
	img = image_download(url1)
	context = {'img': img}
	return render(request, 'app_igdl/image.html', context)
