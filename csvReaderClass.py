import pandas as pd

class csvReaderClass:

    def __init__(self,path) :
        self.data=pd.read_excel(path)
        self.dataDict=self.data.to_dict(orient='records')
        

