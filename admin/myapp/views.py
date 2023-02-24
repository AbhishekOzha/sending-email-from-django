from django.http import HttpResponse
from .utils import send_email_test
# Create your views here.


def abhi(request):
    if request.method=="GET":
        email ="rimeshsapkota12345@gmail.com"
        send_email_test(email)
        return HttpResponse('HI')