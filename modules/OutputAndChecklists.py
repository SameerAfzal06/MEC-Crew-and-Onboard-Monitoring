import os
from collections import deque

CHECKLIST = {
    "oxygenPercent": [
        "Check that oxygen generator is running",
        "If oxygen is too low, check for cabin leaks and put on oxygen masks",
        "If oxygen is too high, turn off oxygen supply and anything that sparks",
    ],
    "bloodOxygen": [
        "Check that the SpO2 sensor is clipped on properly",
        "Crew members stop any activities and rest",
        "Check cabin oxygen levels",
        "Double check SpO2 again after 2 minutes",
    ],
    "bodyTemp": [
        "Check that the temperature sensor is attached properly",
        "Measure temperature with backup thermometer",
        "If too hot, stop exercising and drink water",
        "If too cold, get a blanket and move somewhere warmer",
    ],
    "radiationPerHour": [
        "Verify radiation dosimeter sensor connection",
        "Move crew to the spacecraft radiation storm shelter",
        "Log exposure duration and notify Mission Control",
    ],
    "heartRate": [
        "Have crew member sit down, rest, and hydrate",
        "Re-check pulse manually after 2 minutes",
        "Review recent physical exertion or stress logs",
    ],
    "co2Percent": [
        "Check that CO2 scrubber is running",
        "Make sure backup scrubber is working",
        "Notify Mission Control",
        "Move crew to a safer space",
    ],
}

# holds 20 minutes of data (6,000 readings at 5 Hz) during comms blackouts
blackout_buffer = deque(maxlen=6000)

def run_step3(time_sec, clean_metrics, status_array):
    # saves every clean reading to the local blackout buffer
    blackout_buffer.append({"time_sec": time_sec, **clean_metrics})

    # clears the terminal so it updates in place like a live monitor
    os.system("cls" if os.name == "nt" else "clear")

    print(f"=== HEALTH COPILOT | MISSION TIME: {time_sec}s | BUFFER: {len(blackout_buffer)}/6000 ===")

    # print 6 clean status lines (🟢 for safe, 🔴 for alert)
    for metric, status in zip(CHECKLIST.keys(), status_array):
        icon = "🟢" if status == 1 else "🔴"
        print(f"  {icon} {metric:<18}: {clean_metrics[metric]}")

    # prints an immediate checklist underneath when any sensor hits 0
    if 0 in status_array:
        print("\n⚠️  ACTION REQUIRED:")
        for metric, status in zip(CHECKLIST.keys(), status_array):
            if status == 0:
                print(f"\n  [{metric} — Current: {clean_metrics[metric]}]")
                for step_num, action in enumerate(CHECKLIST[metric], start=1):
                    print(f"    {step_num}. {action}")

