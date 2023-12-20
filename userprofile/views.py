import json
from django.http import HttpResponse, JsonResponse
from userprofile.models import Profile
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

def get_profile(request):
    if request.method == 'GET':
        profile = Profile.objects.get(request.user)
        return HttpResponse(serializers.serialize("json", profile))

def has_profile(request):
    if request.method == 'GET':
        profile = Profile.objects.get(request.user)
        if profile:
            return JsonResponse({"status": "true"}, status=200)
        else:
            return JsonResponse({"status": "false"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=400)

@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        profile = Profile.objects.create(
            user = request.user,
            name = data['name'],
        )

        return HttpResponse(serializers.serialize("json", profile))

@csrf_exempt
def edit_profile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        profile = Profile.objects.get(user=request.user)
        profile.edit_profile(data["name"])

        return JsonResponse({"status": "success"}, status=200)
    
@csrf_exempt
def delete_profile(request):
    if request.method == 'POST':
        user = User.objects.get(user=request.user).delete()
        return JsonResponse({"status": "success"}, status=200)