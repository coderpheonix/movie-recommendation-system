# Movie Recommendation System

A **Flask-based movie recommendation system** that provides intelligent movie suggestions using **TF-IDF** and **collaborative filtering**. This project includes a production-ready REST API and a simple web interface.

---

## Features

- Recommend movies based on **content similarity** (TF-IDF).  
- **Collaborative filtering** for personalized recommendations.  
- **RESTful API** for integration with other applications.  
- Simple web interface to test movie recommendations.  
- Uses **MongoDB** for storing and managing movie data.

---

## Tech Stack

- **Backend:** Python, Flask  
- **Database:** MongoDB  
- **Machine Learning:** scikit-learn (TF-IDF, cosine similarity)  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** Docker (optional)  



## Installation

1. Clone the repository:

```bash
git clone https://github.com/coderpheonix/movie-recommendation-system.git
cd movie-recommendation-system
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
Install dependencies:

bash
pip install -r requirements.txt
Ensure MongoDB is running locally or update the connection string in config/db_config.py.

Usage
Run the Flask app:

bash
python app.py
Open a web browser and go to:

cpp
http://127.0.0.1:5000
Search for a movie and get recommendations.

API Endpoints
Method	Endpoint	Description
GET	/	Home page
POST	/recommend	Get movie recommendations based on input

Example POST request:

json

{
  "movie_title": "Inception"
}
Example response:

json

{
  "recommended_movies": [
    "Interstellar",
    "The Dark Knight",
    "Memento"
  ]
}
Contributing

Fork the repository.

Create a branch: git checkout -b feature/your-feature-name

Make changes and commit: git commit -m "Add feature"

Push to branch: git push origin feature/your-feature-name

Open a Pull Request.

License
This project is licensed under the MIT License.
