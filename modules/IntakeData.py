import csv
import time

CSV_FILE = "modules/demo_telemetry.csv"

#the last good reading for each sensor as a backup
last_valid = {
    "oxygenPercent": None,
    "bloodOxygen": None,
    "bodyTemp": None,
    "radiationPerHour": None,
    "heartRate": None,
    "co2Percent": None,
}

# used to make sure if the sensor value suddenly did not jump more than 10% since the last reading
def is_anomalous_jump(metric, val):
    prev = last_valid[metric]
    if prev is None or prev == 0:
        return False
    return (abs(val - prev) / abs(prev)) > 0.10

# cleans one row of CSV data and returns safe numbers for Step 2
def get_clean_metrics(row):
    # Matches CSV column names to the exact names Step 2 expects
    raw_map = {
        "oxygenPercent": row["o2_pct"],
        "bloodOxygen": row["spo2_pct"],
        "bodyTemp": row["temp_c"],
        "radiationPerHour": row["rad_mgy_day"],
        "heartRate": row["hr_bpm"],
        "co2Percent": row["co2_pct"],
    }

    clean_metrics = {}
    for key, raw_val in raw_map.items():
        # try is used here to convert text to a decimal and also catch broken values like "ERR"
        try:
            val = float(raw_val)
        except (ValueError, TypeError):
            print(f"[CORRUPT] Bad {key} ('{raw_val}') -> keeping {last_valid[key]}")
            clean_metrics[key] = last_valid[key] if last_valid[key] is not None else 0
            continue

        # it blocks unrealistic >10% spikes otherwise it saves as the new good reading
        if is_anomalous_jump(key, val):
            print(f"[FILTERED >10%] {key} jumped {last_valid[key]} -> {val}. Ignored.")
            clean_metrics[key] = last_valid[key]
        else:
            last_valid[key] = val
            clean_metrics[key] = val

    return clean_metrics

# reads the CSV file at 5 readings per second (0.2s pause)
def run_step1():
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            metrics_from_IntakeData = get_clean_metrics(row)
            print(f"[STEP 1 -> STEP 2] {metrics_from_IntakeData}")
            time.sleep(0.2)

if __name__ == "__main__":
    run_step1()