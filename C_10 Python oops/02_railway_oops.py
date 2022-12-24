class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.Name}")
        print(f"train is {self.train}")

harrysApplication = RailwayForm()
harrysApplication.Name = "Harry"
harrysApplication.train = "Graibrath Express"
harrysApplication.printData()

