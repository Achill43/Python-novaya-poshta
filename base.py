import requests
import json

def get_departments(url, api_key, city):
    send_data = {
        "apiKey": api_key,
        "modelName": "AddressGeneral",
            "calledMethod": "getWarehouses",
            "methodProperties": {
                "CityName": city,
            }
        }

    r = requests.post(url, data=json.dumps(send_data))

    result_data = json.loads(r.content)
    departments = result_data['data']
    #print(addresses)
    for department in departments:
        print("Название отделения: "+ str(department['Description']))
        print("Тип отделения: "+ str(department['TypeOfWarehouse']))
        print("Номер отделения: "+ str(department['Number']))
        print("Название населенного пункта: "+ str(department['CityDescription']))
        print()

def get_city(url, api_key):
    send_data = {
        "apiKey": api_key,
        "modelName": "Address",
            "calledMethod": "getCities",
            "methodProperties": {
            }
        }

    r = requests.post(url, data=json.dumps(send_data))

    result_data = json.loads(r.content)
    cities = result_data['data']
    for city in cities:
        print("Назва: "+city['Description'])
        print("Ref: "+city['Ref'])


url = "https://api.novaposhta.ua/v2.0/json/"
api_key = "e8662f75153b7eb4e756dc7702ead076"

#get_city(url, api_key)
get_departments(url, api_key, "Київ")


#payment_type = forms.ModelChoiceField(
#        queryset=PaymentType.objects.all(), empty_label=_('Виберіть спосіб оплати'),
#        )