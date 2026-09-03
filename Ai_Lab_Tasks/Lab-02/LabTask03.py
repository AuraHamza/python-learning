class ResponseAgent:
    def execute_response(self):
        print("Response Agent")
        print("Executing general response...")


class AlertAgent(ResponseAgent):
    def execute_response(self):
        print("\nAlter Agent")
        print("Sending security alert notification.")


class BlockAgent(ResponseAgent):
    def execute_response(self):
        print("\nBlock Agent")
        print("Blocking malicious activity.")


class RecoverAgent(ResponseAgent):
    def execute_response(self):
        print("\nRecover Agent")
        print("Recovering affected system.")


alert = AlertAgent()
block = BlockAgent()
recover = RecoverAgent()

#Manaully called 
# alert.execute_response()
# block.execute_response()
# recover.execute_response()

#Making list then call 
agents=[alert,block,recover]
for agent in agents:
    agent.execute_response()