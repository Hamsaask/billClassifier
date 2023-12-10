import csv

class csvWriterClass:

    def __init__(self,data):
        with open('output.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=['description','amount','quantity','category','predictedCategory'])
            writer.writeheader()
            for row in data:
                writer.writerow(row)

        
