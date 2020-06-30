# Weather Data

In this project, you will use the Python `requests` library to obtain weather data for different locations.
You will store that data as instances of a class and then use `matplotlib` to generate a bar chart of temperatures.
You will need to create and run a Python file called `weather.py` to complete this project.

### Step 1
Sign up for an account and obtain an API key from [Climacell](https://developer.climacell.co/). Read the Climacell [docs](https://developer.climacell.co/v3/reference#get-realtime) on hot to make a request for a specific latitide and longitude's current weather.

### Step 2
Read the docs for the [requests](https://requests.readthedocs.io/en/master/user/quickstart/) library and note how to make a request.

### Step 3
Create a list of tuples called `locations` that contains pairs of (latitude, longitude) for 10 locations of your choice.

### Step 4
Make a request to the realtime endpoint using `requests` to obtain the temp and precipitation for the latitude and longitude (23.0506249, -82.4730905).

### Step 5
Write a function (or set of functions) that makes a request to obtain temp and precipitation for each location in the list `locations`. 
Store the results of these requests.
You may want to think about how a class or classes could help organize your data here.

### Bonus
Use [matplotlib](https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barh.html) to create a graph of the results.





