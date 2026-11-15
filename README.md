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
git clone [https://github.com/SameerAfzal06/MEC-Crew-and-Onboard-Monitoring.git](https://github.com/SameerAfzal06/MEC-Crew-and-Onboard-Monitoring.git)
cd MEC-Crew-and-Onboard-Monitoring
python3 main.py
```

## References

[1] Occupational Safety and Health Administration (OSHA), "1910.146 - Permit-required confined spaces," 2026. https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.146 (accessed Nov. 15, 2026).

[2] Yale Medicine, "Pulse Oximetry," 2026. https://www.yalemedicine.org/conditions/pulse-oximetry (accessed Nov. 15, 2026).

[3] Canadian Nuclear Safety Commission (CNSC), "Radiation doses," 2026. https://www.cnsc-ccsn.gc.ca/eng/nuclear-safety-security/educational-resources/radiation/radiation-doses/ (accessed Nov. 15, 2026).

[4] Cleveland Clinic, "Heart Rate: What's Normal?," 2026. https://my.clevelandclinic.org/health/diagnostics/heart-rate (accessed Nov. 15, 2026).

[5] MedlinePlus, "Body temperature norms," U.S. National Library of Medicine, 2026. https://medlineplus.gov/ency/article/001982.htm (accessed Nov. 15, 2026).

[6] Occupational Safety and Health Administration (OSHA), "Carbon Dioxide - Chemical Data," 2026. https://www.osha.gov/chemicaldata/183 (accessed Nov. 15, 2026).

