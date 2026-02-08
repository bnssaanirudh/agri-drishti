Here is a professional, **Government-Grade README.md** file for your project.

You can copy-paste this directly into a file named `README.md` in your main folder.

---

# 🛰️ Agri-Drishti | National Crop Stress Early-Warning System

**Agri-Drishti** is a national-scale decision support system designed to detect pre-visible crop stress across India. By leveraging **Google Earth Engine (GEE)** and **Sentinel-2 Satellite Imagery**, it provides policymakers with a 2-3 week early warning window for drought and agricultural distress.

---

## 🎯 Objective

To build a resilient, "fail-safe" monitoring dashboard that:

* **Detects** crop stress using real-time multi-spectral satellite indices (NDVI).
* **Analyzes** seasonal deviations against a 5-year historical baseline.
* **Visualizes** risk at a district level for 30+ key agricultural zones in India.
* **Operates** seamlessly with a hybrid online/offline architecture.

---

## ⚡ Key Features

* **🌍 Pan-India Coverage:** Real-time monitoring of 30+ districts across Punjab, UP, Maharashtra, Karnataka, and Tamil Nadu.
* **🛰️ Live Satellite Engine:** Direct integration with Google Earth Engine to process Sentinel-2 imagery (10m resolution).
* **📉 Seasonal Deviation Analytics:** Comparative charts showing Current Season vs. 5-Year Normal.
* **🛡️ Fail-Safe Architecture:** Automatic fallback to local datasets if satellite connection is interrupted or cloudy.
* **🚨 Risk Heatmap:** Color-coded stress intensity map (Critical/Warning/Normal) for instant situational awareness.
* **📄 Policy-Ready Reports:** Automated generation of drought assessment metrics.

---

## 🛠️ Tech Stack

### **Frontend (The Dashboard)**

* **Framework:** Next.js 14 (React)
* **Styling:** Tailwind CSS (Government-grade minimal UI)
* **Mapping:** Leaflet.js with CartoDB Dark/Voyager Tiles
* **Analytics:** Chart.js for time-series visualization

### **Backend (The Intelligence)**

* **API:** FastAPI (Python High-Performance)
* **Satellite Engine:** Google Earth Engine (Python API)
* **Processing:** NumPy & Pandas for data normalization
* **Containerization:** Docker & Docker Compose

---

## 🚀 Getting Started

### Prerequisites

* **Docker Desktop** (Running)
* **Git**
* **Google Earth Engine Service Account Key** (`ee-key.json`)

### 1. Clone the Repository

```bash
git clone https://github.com/bnssaanirudh/agri-drishti.git
cd agri-drishti

```

### 2. Configure Credentials

You must add your Google Earth Engine service account key for live satellite data.

* Place your JSON key file in: `backend/credentials/`
* Rename the file to: `ee-key.json`

### 3. Launch the System

Agri-Drishti uses Docker to set up the entire environment (Frontend, Backend, Database) automatically.

```bash
docker compose up --build

```

### 4. Access the Dashboard

Once the terminal says `Ready`, open your browser:

* **Frontend UI:** [http://localhost:3000](https://www.google.com/search?q=http://localhost:3000)
* **Backend API Docs:** [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)

---

## 📂 Project Structure

```bash
agri-drishti/
├── frontend/                 # Next.js Application
│   ├── app/                  # Pages & Layouts
│   ├── components/           # Map, Charts, Sidebar
│   └── public/               # Assets
├── backend/                  # FastAPI Application
│   ├── app/
│   │   ├── engine/           # GEE Satellite Logic (sentinel.py)
│   │   ├── ml/               # Risk Modeling
│   │   └── main.py           # API Endpoints
│   └── credentials/          # Secure Keys (GitIgnored)
└── docker-compose.yml        # Orchestration Config

```

---

## 🖥️ System Architecture

1. **User Request:** The Policymaker selects a district on the Dashboard.
2. **API Call:** Next.js requests data from FastAPI (`/api/v1/national/risk-summary`).
3. **Satellite Task:** FastAPI triggers the `sentinel.py` engine.
4. **Earth Engine Processing:** The request is sent to Google's Cloud; NDVI is calculated from the latest cloud-free Sentinel-2 pixels.
5. **Risk Scoring:** The raw NDVI is compared against the 5-year average to generate a **Risk Score (0.0 - 1.0)**.
6. **Visualization:** Data is returned to the Frontend and rendered as a heatmap bubble.

---

## 📸 Screenshots

| National Risk Map | Seasonal Analytics |
| --- | --- |
| *(Place your map screenshot here)* | *(Place your chart screenshot here)* |

---

## 🤝 Contributing

This project is open-source for educational and governmental use.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewSatelliteIndex`)
3. Commit your Changes (`git commit -m 'Added NDWI index'`)
4. Push to the Branch (`git push origin feature/NewSatelliteIndex`)
5. Open a Pull Request

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

### 👨‍💻 Developed By

**Badampudi Agasthya Anirudh**
