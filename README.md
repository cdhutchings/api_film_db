# Creating RESTful API to add films to my film DB :unicorn:

### API file

Contains all functions that can be operated through my flask server. These can be accessed through the localhost: 127.0.0.1:5000
`filmpost` is the method which allows for adding films too the database. 

### JSON

To run a successful POST, you must write the correct json for the task. The following is an example of the accepted 
structure



    {"type": "movie",
    "title": "Pan''s Labyrinth",
    "original_title": "El laberinto del fauno",
    "is_adult": 1,
    "year": 2006,
    "end_year": 0,
    "runtime": 116,
    "genre": "Dark Fantasy, Drama"}


### filmpost

if one sends an acceptable json to `127.0.0.1:5000/filmpost`, a connection is made first to the film database.
 The
 data from the json is then extracted and transformed into a usable dictionary format. Using the `insert` method from
  my sql connection class, this data is then queried into the database before finally ensuring it is made persistant 
  with a `.commit()` command. If all is good, the host should return "All good! Check your database!"

