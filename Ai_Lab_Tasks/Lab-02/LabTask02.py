class AMS:
    def __init__(self,thread_id,name,severity):
        self.thread_id=thread_id
        self.name=name
        self.severity=severity

class CropDiseaseThreat(AMS):
    def __init__(self, thread_id, name, severity,disease):
        super().__init__(thread_id, name, severity)
        self.disease=disease
    def detect_disease(self):
        print("\nThread ID:",self.thread_id)
        print("Name:",self.name)
        print("Severity:",self.severity)
        print("Disease: ",self.disease)

class PestThread(AMS):
    def __init__(self, thread_id, name, severity,pest):
        super().__init__(thread_id, name, severity)
        self.pest=pest
    def detect_pest(self):
         print("\nThread ID:",self.thread_id)
         print("Name:",self.name)
         print("Severity:",self.severity)
         print("Pest: ",self.pest)

class WaterStressThreat(AMS):
    def __init__(self, thread_id, name, severity,moist):
        super().__init__(thread_id, name, severity)
        self.moist=moist
    def check_soil_moisture(self):
         print("\nThread ID:",self.thread_id)
         print("Name:",self.name)
         print("Severity:",self.severity)
         print("Water_level: ",self.moist)

disease = CropDiseaseThreat("T001", "Wheat", "High", "Rust")
pest = PestThread("T002", "Cotton", "Low", "Bollworm")
water = WaterStressThreat("T003", "Rice", "High", "Low")

disease.detect_disease()
pest.detect_pest()
water.check_soil_moisture()