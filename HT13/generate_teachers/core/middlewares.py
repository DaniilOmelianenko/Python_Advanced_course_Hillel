from time import time

from core.models import Logger

from django.utils.deprecation import MiddlewareMixin


class LogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.start_time = time()

    def process_response(self, request, response):
        if not request.path.startswith('/admin/'):
            request.end_time = time()
            save_data = Logger(
                path=request.path,
                method=request.method,
                execution_time=(request.end_time - request.start_time)
            )
            save_data.save()
        return response
