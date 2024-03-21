import requests



class APIRetrieval:

    baseUrl = "https://swapi.dev/api/"
    PeopleUrl = "people/"
    StarshipUrl = "starships/"


    #def findPerson(self,IDnumber):
    #response = requests.get(baseUrl+people+IDnumber)





    # def BaseUrl(self,resource_name:str):
    #     if resource_name is None:
    #         return None
    #     else:
    #         try:
    #             url = f"https://swapi.dev/api/{resource_name}"
    #             resource_list = []
    #             while url is not None:
    #                 response = requests.get(url)
    #                 if response.status_code in (200,201):
    #                     resource_json = response.json()
    #                     url = response.json()['next']
    #                     resource_list.extend(resource_json["results"])
    #                 else:
    #                     print(f'unexpected error:{response.status_code}')
    #                     return None
    #             return resource_list
    #         except requests.exceptions.HTTPError as e:
    #             print("HTTP Error: ", e)
    def get_starships_info(self,resource_url:str):
        if resource_url is None:
            return None
        else:
            try:
                response = requests.get(resource_url)
                if response.status_code in (200,201):
                    resource_json = response.json()
                    return resource_json
                else:
                    print(f'unexpected error:{response.status_code}')
                    return None
            except requests.exceptions.HTTPError as e:
                print("HTTP Error: ", e)

base_url_result = APIRetrieval()
print(base_url_result.BaseUrl("people"))
resource_content = APIRetrieval()
print(resource_content.get_starships_info("https://swapi.dev/api/people/3/"))