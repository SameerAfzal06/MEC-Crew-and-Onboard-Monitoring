import csv
import time
from modules.IntakeData import get_clean_metrics, CSV_FILE
from modules.AnalyzeData import analyze_data
from modules.OutputAndChecklists import run_step3

def run_copilot():
    print("Starting Health Copilot (5 Hz Mars Transit Telemetry)...")
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            clean_metrics = get_clean_metrics(row)                        # Step 1
            status_array = analyze_data(clean_metrics).verify_safety()    # Step 2
            run_step3(row["time_sec"], clean_metrics, status_array)       # Step 3
            time.sleep(0.1)                                               # 10 readings/sec
    print("Telemetry stream complete.")

if __name__ == "__main__":
    run_copilot()