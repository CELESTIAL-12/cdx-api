# blacklist_middleware.py

class BlacklistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request URL is blacklisted
        if self.is_url_blacklisted(request.path):
            # Handle the case when the URL is blacklisted (e.g., return an error response)
            return self.blacklisted_response()
        else:
            # Proceed with the request
            response = self.get_response(request)
            return response

    def is_url_blacklisted(self, url):
        # Implement your logic to check if the URL matches any blacklisted URL
        # You can use a database lookup or a list of blacklisted URLs
        # For this example, we will use a simple list for demonstration purposes.
        blacklisted_urls = [
            "https://www.berkeley.edu/",
            "http://calbears.com/traditions/history-of-cal-football",
            "http://espn.go.com/college-sports/recap?id=40076958",
            "https://en.wikipedia.org/",
            "https://www.youtube.com/",
            
            # Add more blacklisted URLs as needed
        ]
        return any(url.startswith(blacklisted_url) for blacklisted_url in blacklisted_urls)

    def blacklisted_response(self):
        # Implement the response for blacklisted URLs
        # You can return an error response or a custom message as per your requirement.
        # For demonstration, we will return a plain text response with a 403 status code.
        return HttpResponse("This URL is blacklisted.", status=403)
