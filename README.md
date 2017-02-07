# hello-world
This is my first Github Repository
Here I am going to write something about myself... looking forward on how this will go...


#deploy to Heruko

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# What does the service do?
It's a availability fulfillment service that uses a build in array to determine whether a product is available in a country. The services takes the `geo-country` parameter from the action, performs geolocation for the city and requests the availability information from the array. 

The service packs the result in the Api.ai webhook-compatible response JSON and returns it.
