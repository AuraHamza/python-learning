class Agents:
    def __init__(self,agent_id,patient_name,status):
        self.agent_id=agent_id
        self.patient_name=patient_name
        self.status=status


class HeartMonitoringAgent(Agents):
    def __init__(self,agent_id,patient_name,status,heart_rate):
        self.heart_rate=heart_rate
        super().__init__(agent_id, patient_name, status)
    def mointor_heart_rate(self):
        print("\nAgent ID:",self.agent_id)
        print("Patient:",self.patient_name)
        print("Status:",self.status)
        print("Heart Rate:",self.heart_rate)

class MedicineReminderAgent(Agents):
    def __init__(self,agent_id,patient_name,status,medicine_name):
            self.medicine_name=medicine_name
            super().__init__(agent_id, patient_name, status)
    def remind_medicine(self):
            print("\nAgent ID:",self.agent_id)
            print("Patient:",self.patient_name)
            print("Status:",self.status)
            print("Medicine:",self.medicine_name)
            print("Reminder: Please take your medicine at 8:00 PM.")

class HealthPredictionAgent(Agents):
    def predict_health_risk(self):
     print("\nAgent ID:",self.agent_id)
     print("Patient:",self.patient_name)
     print("Status:",self.status)
     print("Analyzing patient data...")
     print("Possible health risks detected.")


heart=HeartMonitoringAgent("A111","Hamza","Active",82)
medicine=MedicineReminderAgent("A222","Ali","Active","Panadol")
health=HealthPredictionAgent("A333","Umer","Active")

heart.mointor_heart_rate()
medicine.remind_medicine()
health.predict_health_risk()