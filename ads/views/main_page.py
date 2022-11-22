from django.http import JsonResponse


def main(request):
    return JsonResponse({"status": "Ok"}, status=200)