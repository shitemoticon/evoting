<h1>Description
  <p>This is a project I've been working on and decided to share. I have shared only the API, this project also have a vuejs front end.
    The API is built with django rest framework, requirements are in requirement.txt </p>
  
<h1>How to use
  <li>Clone this repo
  <li>Install the requirement <code>pip install -r requirement.txt</code>
  <li>Rename <code>my-settings.py</code> to <code>settings.py</code> NOTE: There is no secret key . If you created your project with django-admin don't bother with this step.
  <li>In the file you just renamed (now <code>settings.py</code>) update the datebase settings in the DATABASES dictionary. Exact options depends on the database you use (Do some googling).  
  <li>If you're developing the front and backend on the same system add your frontend's url to the CORS_ALLOWED_ORIGINS list as a string (without this requests from the frontend will be blocked).
  <li>If everything in <code>settings.py</code> is set correctly make your database migrations and migrate with the commands <code>python manage.py makemigrations</code> and <code>python manage.py migrate</code>. All tables will be created in your database.
  <li>All endpoints are in <code>urls.py</code>. You can use those for your frontend app.
    
<h1>Note:
  <h3>This project is not complete yet but the login and registration endpoints are fully functional</h3>
 
    
