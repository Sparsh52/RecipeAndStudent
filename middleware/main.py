class ExampleMiddleware:
    def __init__(self, get_response) -> None:
         self.get_response = get_response

    def __call__(self, request,*args, **kwds):
        print("Middleware called")
        return self.get_response(request)