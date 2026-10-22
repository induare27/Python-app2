'''Q2. Create a multilevel chain:
class Device → class Phone → class Smartphone
Add one method in each and create an object of Smartphone to show all.'''

class Device:
    def dev_type(self,type):
        self.type=type
        print("Device type:",self.type)
class Phone(Device):
    def phn_model(self,model):
        self.model=model
        print("Phone model:",self.model)
class Smartphone(Phone):
    def sm_model(self,sm_phn):
        self.sm_phn=sm_phn
        print("Smart phone model:",self.sm_phn)
s=Smartphone()
s.dev_type("mobile")
s.phn_model("Nokia old version")
s.sm_model("samsung galaxy")