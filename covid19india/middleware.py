import requests
import json

class Covid19Middleware:
    def __init__(self,get_response):
        self.get_response = get_response
        response = requests.get('https://api.covid19india.org/state_district_wise.json')
        with open(r"covid19india\raw\package.json", "w") as outfile:
            outfile.write(response.text)


    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        return response