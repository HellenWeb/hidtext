
# Modules

from django.http import HttpResponse

# Logic

def index(req):
    with open("hidtext/site.txt", "r") as f:
        return HttpResponse(f.read())
