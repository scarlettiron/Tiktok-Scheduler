from django.shortcuts import render

def upload_tiktok(self, request):
    if request.method == 'GET':
        return render(template_name='upload_tiktok.html')
    
    if request.method == 'POST':
        pass
