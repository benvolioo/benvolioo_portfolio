from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import FileResponse, Http404

# Create your views here.
def resume_view(request):
    with open('media/Marty_Rudolf_Resume.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type = 'application/pdf')
        response['Content-Disposition'] = 'filename=Marty_Rudolf_Resume.pdf'
        return response
