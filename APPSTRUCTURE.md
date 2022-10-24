# Django REST API App Structure Explanations

Django is an MVC architecture which means apps are built upon Models (used for data architecture), Views (implementations of these Models), and Controllers (routing for the views and models)

Refer to [Mozilla Developer in-depth explanation on MVC](https://developer.mozilla.org/en-US/docs/Glossary/MVC)

## How the MVC architecture is implemented
models.py contains the classes that define the architecture of our Data. 
In the "drinks" folder, we have models.py that contains a Drink class. The Drink class states that a Drink will have a name and description. With the model created, we can now add Drinks to our database

> Run the development server and go to the site's [admin page](http://localhost:8000/admin/) to add new Drinks to the database.

The next step is to perform actions on the drinks that are made.
This is where views.py comes into play. In views.py, we perform actions and we also decide what kinds of requests the functions can receive. We tie these functions to the routing of the application.

In the "drinks" folder, there exists a views.py which defines the function __drink_list__ that accepts "GET" and "POST" requests. The function gets all of the Drinks from the database, serializes the data, and returns the JSON response object

> The reason for serializing the data is due to this being a REST API. API data needs to be searialized to prepare the format of the data (JSON in this case).

In the "drinks" folder, we have serializers.py and we define a class which prepares the format of the response when Drink objets are used.

Once models and views have been created, it's time to create endpoints and routes so that clients can interact with the API. This is where urls.py comes into play. urls.py is the file in an app that defines what url endpoints can be used.

In the "drinks" folder, there is a urls.py which contains the endpoints for the "admin/" endpoint and the "drinks/" endpoint
When we defined the "drinks/" endpoint, we attached the view we created for drinks: the __drinks_list(...)__ function.
