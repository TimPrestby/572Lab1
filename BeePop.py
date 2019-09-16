import csv


with open('C:/Users/tprestby/Documents/GitHub/572Lab1/Data/county/Osmia_lignaria-California.csv') as data:
    readCSV = csv.reader(data, delimiter=',')

    counties = ["6001","6003","6005","6007","6009","6011","6013","6015","6017","6019","6021","6023","6025","6027","6029","6031","6033","6035","6037","6039","6041","6043","6045","6047","6049","6051","6053","6055","6057","6059","6061","6063","6065","6067","6069","6071","6073","6075","6077","6079","6081","6083","6085","6087","6089","6091","6093","6095","6097","6099","6101","6103","6105","6107","6109"]
    dataList = []

    data.readline()
    
    for row in data:
        #print row[:5]
        dataList.append(row[1:5])
    #print dataList

    for item in counties:
        count = dataList.count(item)
        print str(item) + "," + str(count)



