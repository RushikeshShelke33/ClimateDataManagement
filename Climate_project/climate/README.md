Django Climate App
This project is a Proof of Concept (POC) on climate changes, focusing on four climate types: hot, humid, rainy, and cold. The application allows syncing climate data reports into the system and provides various endpoints to retrieve and manipulate the data.

Setup Instructions
Clone the repository:

bash
Copy code
git clone <repository_url>
cd django-climate-app
Set up a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Run database migrations:

bash
Copy code
python manage.py migrate
Seed the database with initial data:

bash
Copy code
python seed_db.py
Running the Server
Start the Django development server:

bash
Copy code
python manage.py runserver
The server will start, and you can access the application at http://127.0.0.1:8000/.

Endpoints
Add Climate Data:
Endpoint: /add_data/
Method: POST

Use this endpoint to add climate data. Send a JSON payload containing climate information.

Example Payload:

json
Copy code
{
    "climate": "hot",
    "area_code": 455621,
    "temperature": 25,
    "humidity": 88,
    "chances_of_rain": 40
}
List All Climate Data:
Endpoint: /list_data/
Method: GET

Use this endpoint to retrieve a list of all climate data entries.

List Climate Data by Area:
Endpoint: /data/by_area/<area_code>/
Method: GET

Use this endpoint to retrieve climate data for a specific area using its area code.

Example: /data/by_area/455621/

List Climate Data by Area and Climate:
Endpoint: /data/by_area_and_climate/<area_code>/<climate>/
Method: GET

Use this endpoint to retrieve climate data for a specific area and climate.

Example: /data/by_area_and_climate/455621/hot/

Calculate Climate Delta:
Endpoint: /climate_delta/
Method: POST

Use this endpoint to calculate climate deltas and climate change index based on specified "from" and "to" climates.

Example Payload:

json
Copy code
{
    "from_climate": "hot",
    "to_climate": "cold",
    "area_code": 455621
}
Note
This POC is not a tool for accurate climate analysis. It's a demonstration of Django REST Framework features and concepts.