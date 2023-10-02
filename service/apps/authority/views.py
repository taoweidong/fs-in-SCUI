# Create your views here.
from django.http import JsonResponse


def token(request):
    response = {
        "code": 200,
        "data": {
            "token": "SCUI.Administrator.Auth",
            "userInfo": {
                "userId": "1",
                "userName": "Administrator",
                "dashboard": "0",
                "role": [
                    "SA",
                    "admin",
                    "Auditor"
                ]
            }
        },
        "message": ""
    }
    return JsonResponse(response)


