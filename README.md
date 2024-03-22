# Starships

![X-Wing](https://www.denofgeek.com/wp-content/uploads/2019/12/x-wing.jpg?w=1024)
### Project Goal

This collaborative project aims to:

Interact with the SWAPI api using python 'requests'
Parse starship data from the API response.
Integrate with MongoDB using PyMongo for data storage.
Efficiently handle pilot information by:
Replacing pilot URLs with corresponding object IDs if they exist in the pre-populated "characters" collection within MongoDB.

Trello was used within an agile working method, and can be viewed here:
https://trello.com/b/GJBdRjhD/room-2-project

### Project Structure

The overall structure of the project was to use object-oriented classes, to be built using test-driven development.


The *swapi*, the Star Wars API! is the world's first quantified and programmatically-accessible data source for all the data from the Star Wars canon universe! This project provides the valuable insights for the starwars based on the content being added to the MongoDB for starship details and by creating the reference between character details and starship details.
1. Access the *swapi* in order to understand what content is available.
2. Create the collection *starships* on MongoDB compass.
3. Feed into database collection, creating the reference between the characters and starship through the pilot id. 
4. Query API to return specific and overall responses to get many kinds of Star Wars info.
5.  Create collections for the business to view and analyse the data for characters and starship. 

# Python libraries to run the project:
1.  *unittests* for testing class methods
2.  *requests* for retrieving from the Star Wars API
3.  *pymongo* for interacting with MongoDB database.

## How to use the starships project :

clone the repo
````
git clone https://github.com/robbfox/starships.git
````

Install the required Python packages:
````
pip install -r requirements.txt
````
Make sure Mongo is installed


1.  Star Wars data integration
    1. API data retrieval
    2. Data transformation and storage
## API data retrieval:
In this class, APIRetrieval with two main functions:
BaseUrl = "https://swapi.dev/api/"
PeopleUrl = "people/"
StarshipUrl = "starships/"
1.  *get_resource_list*: This method returns the complete details of the resource name provided. 
e.g. : get_resource_list("people") -  returns the list of dictionaries for all the character details through API.
2. *get_resource_info*: This method returns the complete details of specific individual with the URL.
e.g. : *get_resource_info("https://swapi.dev/api/people/1/")* - returns the details of the individual.
3.  *get_starships_info*: This function utilises the *get_resource_list* method and returns the details for starships.
4.  *get_specific_starship_info*: This function utilises the *get_resource_info* method and returns the details for individual starship.
5.  *get_people_info*: This function utilises the *get_resource_list* method and returns the details for the people.
6.  *get_specific_people_info*: This function utilises the *get_resource_info* method and returns the details for the individual people(character). 

## DataTransformation:
This class takes the data returned from 'API Data Retrieval', and transforms it to a format that can easily be inserted into MongoDB collection.
It contains a number of methods:
1. *check_if_name_in_db(input_name)* this queries the Mongo characters to see if name is present in database
2. *get_id_from_name_in_DB(self, name)* this retrieves the id if it matches the character name in database
3. *data_body_prep(self, name_of_ship=None, model=None, ids=None):* this re-formats the details ready to be inserted into Mongo *starships* collection
4. *insert_into_mongodb(self, data)* this adds each formatted document into the Mongo database collection, having replaced the pilot url taken from *swapi* with the character id from the Mongo character collection







