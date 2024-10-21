import time 

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        start_time = time.time()
        method = request.method
        path = request.path

        response = self.get_response(request, *args, **kwargs)

        duration = time.time() - start_time
        print(f"request with {method} {path} был завершён за {duration:2f} секунд")

        return response