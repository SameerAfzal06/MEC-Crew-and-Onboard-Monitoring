# CREW-SAVE — Mars Transit Crew & Onboard Monitoring

Health Copilot is an offline crew and cabin monitoring system built for the McMaster Engineering Competition (MEC) 2026. Designed for long-duration Mars transit, it reads 5 Hz sensor data, filters out corrupted values and sudden spikes, and checks vitals and cabin levels against real clinical and safety limits. It also saves up to 20 minutes of data locally during Earth–Mars communication blackouts and pulls up step-by-step action checklists the moment any reading goes out of bounds.

# Key Features
* **Fault-Tolerant Data Intake (`IntakeData.py`):** Handles non-numeric sensor faults (`"ERR"`, missing values) and rejects anomalous single-tick spikes (>10% change per 0.2s) by holding the last verified safe reading.
* **Safety Threshold Verification (`AnalyzeData.py`):** Evaluates six physiological and environmental metrics in real time against cited OSHA and clinical limits.
* **20-Minute Blackout Buffer (`OutputAndChecklists.py`):** Uses a fixed-size `collections.deque(maxlen=6000)` rolling buffer to store 20 minutes of 5 Hz telemetry locally during Earth-Mars communication blackouts without unbounded memory growth.
* **Live Crew Dashboard & Checklists:** Displays a clean real-time status board (`🟢` safe / `🔴` alert) with mission elapsed time and automatically surfaces step-by-step troubleshooting procedures upon threshold breaches.

## How to Run
This project uses only Python 3 standard libraries (`csv`, `time`, `collections`)—no external installations are required.

```bash
git clone https://github.com/muhammadabubakarzaka/MEC-Crew-and-Onboard-Monitoring.git
cd MEC-Crew-and-Onboard-Monitoring
python3 main.py
```

