# disastor
# Real-Time Disaster Information Aggregation

## 📌 Project Overview
This project is a **Real-Time Disaster Information Aggregation System** that fetches and displays **real-time disaster-related tweets**. It extracts relevant information about natural disasters such as **earthquakes, floods, and wildfires** and presents them in a structured format.

## ⚡ Features
- Fetches disaster-related tweets from **Twitter API**
- Extracts **location, timestamp, and disaster type**
- Displays tweets on a **simple React dashboard**
- Uses Flask backend to handle API calls
- Allows easy extension with **Google Maps & AI filtering**

## 🛠️ Tech Stack
- **Frontend:** React.js
- **Backend:** Flask (Python)
- **Data Source:** Twitter API (or mock JSON for testing)
- **Additional:** Flask-CORS for cross-origin requests

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/disaster-aggregation.git
cd disaster-aggregation
```

### 2️⃣ Backend Setup (Flask)
#### Install Dependencies
```sh
pip install flask requests flask-cors
```

#### Run the Flask Server
```sh
python app.py
```
The Flask server will start at **http://127.0.0.1:5000**.

### 3️⃣ Frontend Setup (React)
#### Install Dependencies
```sh
npx create-react-app disaster-app
cd disaster-app
npm install
```

#### Start the React App
```sh
npm start
```
The React app will start at **http://localhost:3000**.

---

## 📡 API Endpoints
| Method | Endpoint         | Description                          |
|--------|----------------|----------------------------------|
| GET    | `/tweets`       | Fetches recent disaster-related tweets |

Example JSON Response:
```json
[
  {"text": "Earthquake reported in California!", "id": "12345"},
  {"text": "Flood warning issued for Mumbai!", "id": "67890"}
]
```

---

## 🔥 Troubleshooting
- **ModuleNotFoundError: No module named 'requests'**  
  Run `pip install requests`
- **Flask API Not Found Error**  
  Make sure Flask is running (`python app.py`)
- **CORS Policy Error**  
  Install `flask-cors` and add `CORS(app)` in `app.py`

---

## 📌 Future Enhancements
✅ Integrate Google Maps API for location tracking  
✅ Add AI-based fake news filtering  
✅ Send disaster alerts via SMS using Twilio  

---

## 📜 License
This project is open-source and available under the MIT License.


