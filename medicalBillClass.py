from billClassifierClass import BillClassifierClass

class medicalBillClass:
    description=""
    amount=""
    quantity=""
    inputCategory=""
    predictedCategoryUsingRegex=""
    predictedCategoryUsingML=""

    def __init__(self,inputDict) -> None:
        self.description=inputDict['description']
        self.amount=inputDict['amount']
        self.quantity=inputDict['quantity']
        self.inputCategory=inputDict['category']

    def classifyBillUsingRegex(self):
        billClassifyUsingRegex=BillClassifierClass()
        self.predictedCategoryUsingRegex=billClassifyUsingRegex.classifyBill(self.description)
        return self.predictedCategoryUsingRegex
    
    def convertObjToDict(self):
        return {
            'description':self.description,
            'amount':self.amount,
            'quantity':self.quantity,
            'category':self.inputCategory,
            'predictedCategory':self.predictedCategoryUsingRegex
        }