import requests



class APIRetrieval:

    BaseUrl = "https://swapi.dev/api/"
    PeopleUrl = "people/"
    StarshipUrl = "starships/"

    def Get_Json_from_full_URL(self,URL):
        response = requests.get(URL)
        JsonData = response.json()
        return JsonData

    def get_resource_list(self,resource_name:str):
        if resource_name is None:
            return None
        else:
            try:
                url = APIRetrieval.BaseUrl+resource_name
                resource_list = []
                while url is not None:
                    response = requests.get(url)
                    if response.status_code in (200,201):
                        resource_json = response.json()
                        url = response.json()['next']
                        resource_list.extend(resource_json["results"])
                    else:
                        print(f'unexpected error:{response.status_code}')
                        return None
                return resource_list
            except requests.exceptions.HTTPError as e:
                print("HTTP Error: ", e)

    def get_people_info(self):
         return self.get_resource_list(APIRetrieval.PeopleUrl)

    def get_resource_info(self, resource_url: str):
        if resource_url is None:
            return None
        else:
            try:
                response = requests.get(resource_url)
                if response.status_code in (200, 201):
                    resource_json = response.json()
                    return resource_json
                else:
                    print(f'unexpected error:{response.status_code}')
                    return response
            except requests.exceptions.HTTPError as e:
                print("HTTP Error: ", e)

    def get_starships_info(self):
         return self.get_resource_list(APIRetrieval.StarshipUrl)

    def get_specific_starship_info(self,starship_number):
         starship_url = APIRetrieval.BaseUrl + APIRetrieval.StarshipUrl + str(starship_number)
         return self.get_resource_info(starship_url)

    def get_specific_people_info(self, people_number):
         people_url = APIRetrieval.BaseUrl + APIRetrieval.PeopleUrl + str(people_number)
         return self.get_resource_info(people_url)

    def get_people_info(self):
         return self.get_resource_list(APIRetrieval.PeopleUrl)

