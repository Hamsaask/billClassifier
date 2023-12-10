import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle


class BillClassifierClass:
    outputClass=""
    
    def __init__(self) -> None:
        self.__ambulanceChargeRegex="^.*ambulance.*$"
        self.__anaesthesiaRegex="^.*anaesthe(tic|sia).*$"
        self.__bloodRegex="^.*blood.*$"
        self.__doctorFeeRegex="^.*doctor.*$"
        self.__foodRegex="^.*milk.*$"
        self.__roomRegex="^.*room.*$"
        self.__procedureRegex="^.*colonoscopy.*$"
        self.__medicineRegex=".*diaper.*$"
        self.__outputDictionary={
            self.__ambulanceChargeRegex:'Ambulance',
            self.__anaesthesiaRegex:'Anaesthesia',
            self.__bloodRegex:'Blood & Blood Products',
            self.__doctorFeeRegex:'Doctor Fees',
            self.__foodRegex:'Food & Beverages',
            self.__roomRegex:'Room Rent',
            self.__procedureRegex:'Procedure Charges',
            self.__medicineRegex:'Medicine & Consumables'
        }
        

    def classifyBill(self,inputString):
        for regex in self.__outputDictionary.keys():
            if re.match(regex,inputString,re.IGNORECASE):
                self.outputClass=self.__outputDictionary[regex]
                break
        return self.outputClass
    
    
    def classifyBillUsingML(self,data):
        medical_text = data.iloc[:,0].tolist()
        medical_categories = data.iloc[:,-1].tolist()
        ## Uncomment the below lines to re train the model. 
        # X_train, X_test, y_train, y_test = train_test_split(
        # medical_text, medical_categories, test_size=0.2, random_state=42)
        # model = make_pipeline(TfidfVectorizer(), SVC(kernel='linear'))
        # model.fit(X_train, y_train)
        # with open('medical_classifier_model.pkl', 'wb') as model_file:
        #     pickle.dump(model, model_file)
        with open('medical_classifier_model.pkl', 'rb') as model_file:
            loaded_model = pickle.load(model_file)
        predictions = loaded_model.predict(medical_text)
        print("Classification Report:")
        print(classification_report(medical_categories, predictions))

            
