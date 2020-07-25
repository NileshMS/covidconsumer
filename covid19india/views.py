import json

from django.shortcuts import render

from covidconsumer.settings import COVID_FILE # file name mentioned and path is assigned in settings,
# it will make easy to change path easily by changing path in settings.py


# Create your views here.
def statesList(request):
    dict_data = json.loads(open(COVID_FILE).read())
    # print(type(dict_data))
    states = [state for state in dict_data]
    states.pop(0)
    return render(request, 'index.html', {'states': states})


def districts(request, my_state):
    dict_data = json.loads(open(COVID_FILE).read())
    all_districts = [district for district in dict_data[my_state]['districtData']]
    # print(all_districts)
    return render(request, 'state_info.html', {'districts': all_districts, 'state': my_state})


def district_info(request, my_state, my_district):
    dict_data = json.loads(open(COVID_FILE).read())
    district = [(i, j) for i, j in dict_data[my_state]['districtData'][my_district].items()]
    districtsu = [j for i, j in dict_data[my_state]['districtData'][my_district].items()]
    districtsum=sum(districtsu[1:5])
    district.pop(0)
    delta1=district.pop(4)
    delta = delta1[1]
    deltasum= sum([y for x,y in delta.items()])
    # print(deltasum)
    total = deltasum+districtsum
    return render(request, 'districtInfo.html', {'district_info': district, "district": my_district, 'detail':delta, 'total':total})
