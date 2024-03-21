import requests



class APIRetrieval:

    BaseUrl = "https://swapi.dev/api/"
    PeopleUrl = "people/"
    StarshipUrl = "starships/"



    def get_people_info(self):
        all_people = []

        try:
            # Initial request to get the first page of people
            response = requests.get(self.BaseUrl + self.PeopleUrl)
            response.raise_for_status()  # Raise an error if response status is not successful
            starships_data = response.json()
            all_people.extend(starships_data['results'])

            # Check if there are more pages of results
            while starships_data['next']:
                response = requests.get(starships_data['next'])
                response.raise_for_status()  # Raise an error if response status is not successful
                starships_data = response.json()
                all_people.extend(starships_data['results'])

            return all_people

        except requests.exceptions.RequestException as e:
            print("Error: Cannot connect to the API")
            print(e)
            return None

    def get_specific_people_info(self, person_id):
        try:
            response = requests.get(self.BaseUrl + self.PeopleUrl + str(person_id))
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to retrieve data for person ID {person_id}.")
                return response
        except requests.exceptions.RequestException as e:
            print("Error: Cannot connect to the API.")
            return None

        except requests.exceptions.RequestException as e:
            print("Error: Cannot connect to the API")
            print(e)
            return None







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

# base_url_result = APIRetrieval()
# print(base_url_result.BaseUrl("people"))
# resource_content = APIRetrieval()
# print(resource_content.get_starships_info("https://swapi.dev/api/people/3/"))