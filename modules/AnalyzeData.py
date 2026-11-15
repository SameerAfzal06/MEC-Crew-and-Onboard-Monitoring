class analyze_data:
    """reads the data file and"""

    def __init__(self, metrics):
        self.metrics = metrics_from_IntakeData
    
    def verify_safety(self);
        #defines safe operational bounds
        thresholds = {
            "oxygenPercent" : {"minimum": 19.5 ,"maximum": 20.5 },
            "bloodOxygen" : {"minimum": 88 ,"maximum": 100 },
            "bodyTemp" : {"minimum": 36 ,"maximum": 37.2 },
            "radiationPerHour" : {"minimum": 0.05 ,"maximum": 0.41 },
            "heartRate" : {"minimum": 60 ,"maximum": 100 },
        }

        status_array = []

        #Check oxygen percent
        ox_val = self.metrics.get("oxygenPercent",0)
        if thresholds["oxygenPercent"]["minimum"] <= ox_val <= thresholds["oxygenPercent"]["maximum"]:
            status_array.append(1)
        else:
            status_array.append(0) 

        if 

