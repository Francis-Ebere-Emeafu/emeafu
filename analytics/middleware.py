from .models import Visitor
from django.utils.timezone import now


class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        ip = self.get_ip(request)
        ua = request.META.get('HTTP_USER_AGENT', '')[:500]
        today = now().date()

        if ip:
            Visitor.objects.get_or_create(
                ip_address = ip,
                user_agent = ua,
                date = today
            )

        return response
    
    def get_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')