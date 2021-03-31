# Martial Art project #


### how to start the project
  - install python-venv or virtualenv
  - create a virtual env and run it
  - install the requirements
  - apply th migrations and create a create a super user
  - enjoy coding :)

### the project
this project contain mainly 3 parts:
  - the admin interface
  - the user interface
  - API
there should be an other React app that will be a full user interface(https://github.com/Yassine-cheffai/martial-art-ui)

### API
using django rest framework

### deployement on heroku
this project is deployed on heroku (https://martial-art.herokuapp.com/), the CI process is linked to heroku, so evry time the pipeline ci finish with success on the main branch, the deployement heroku environmnent get updated

### DB
the production should use postgresql DB, may be using the one provided by heroku

### unit test
mainly using the standard django unit test, maybe with an sqlite database even that we have to be carefull about using specific postresql fields types, this may cause issues
