from flask import Flask
import csvReaderClass as cr
import medicalBillClass as mbc
import billClassifierClass as bc
import sys
import csvWriterClass as cw

#path=sys.argv[1]
path='Interview_exercise 1 dataset.xlsx'
#app = Flask(__name__)

#@app.route('/', methods=['GET', 'POST'])
def classify(type):
    if type=='Regex':
        listOfDataDict=cr.csvReaderClass(path).dataDict
        listOfOutputDict=[]
        for dataDict in listOfDataDict:
            obj=mbc.medicalBillClass(dataDict)
            obj.classifyBillUsingRegex()
            listOfOutputDict.append(obj.convertObjToDict())
        cw.csvWriterClass(listOfOutputDict)   
    else:
        data=cr.csvReaderClass(path).data
        obj=bc.BillClassifierClass()
        obj.classifyBillUsingML(data)



if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=105)
    classify('Regex')
    