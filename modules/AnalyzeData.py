class analyze_data:
    """reads the data file and"""

    def __init__(self, metrics):
        self.metrics = metrics
    
    def verify_safety(self):
        #defines safe operational bounds
        thresholds = {
            "oxygenPercent": {"minimum": 19.5, "maximum": 20.5},
            "bloodOxygen": {"minimum": 88, "maximum": 100},
            "bodyTemp": {"minimum": 36, "maximum": 37.2},
            "radiationPerHour": {"minimum": 0.05, "maximum": 0.41},
            "heartRate": {"minimum": 60, "maximum": 100},
            "co2Percent": {"minimum": 0.0, "maximum": 0.5},
        }

        status_array = []

        #Check oxygen percent 
        ox_val = self.metrics.get("oxygenPercent",0)
        if thresholds["oxygenPercent"]["minimum"] <= ox_val <= thresholds["oxygenPercent"]["maximum"]:
            status_array.append(1)
        else:
            status_array.append(0) 

        #Check blood oxygen percent 
        bloodox_val = self.metrics.get("bloodOxygen",0)
        if thresholds["bloodOxygen"]["minimum"] <= bloodox_val <= thresholds["bloodOxygen"]["maximum"]:
            status_array.append(1)
        else:
            status_array.append(0) 

        #Check body temperature 
        bodytemp_val = self.metrics.get("bodyTemp",0)
        if thresholds["bodyTemp"]["minimum"] <= bodytemp_val <= thresholds["bodyTemp"]["maximum"]:
            status_array.append(1)
        else:
            status_array.append(0)
        
        #Check radiation dosage per hour 
        rad_val = self.metrics.get("radiationPerHour",0)
        if thresholds["radiationPerHour"]["minimum"] <= rad_val <= thresholds["radiationPerHour"]["maximum"]:
            status_array.append(1)
        else:
            status_array.append(0) 

        #Check heart rate 
        heartrate_val = self.metrics.get("heartRate",0)
        if thresholds["heartRate"]["minimum"] <= heartrate_val <= thresholds["heartRate"]["maximum"]:
            status_array.append(1)
        else:
            status_array.append(0)

        #Check CO2 percentage
        co2_val = self.metrics.get("co2Percent",0)
        if thresholds["co2Percent"]["minimum"] <= co2_val <= thresholds["co2Percent"]["maximum"]:
            status_array.append(1)
        else:
            status_array.append(0)

        return status_array


