# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:06:38 2018

@author: Siddharth
"""

import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import FormatStrFormatter, ScalarFormatter

def loadData():
# api-key to mentioned to run this example
    BiharMasterDataXML = "https://api.data.gov.in/resource/3f328009-8f64-426d-9228-750a3fe8e326?api-key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx1&format=xml&offset=0&limit=10"

        
#    BiharMasterDataCSV = "https://api.data.gov.in/resource/3f328009-8f64-426d-9228-750a3fe8e326?api-key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&format=csv&offset=0&limit=10"
#    heads = {'accept':"text/csv"}    
#    resp = requests.get(url=BiharMasterDataCSV, headers=heads)
#    data = resp.text   
#    with open('BiharData.csv', 'w', encoding="ISO-8859-1", newline='') as csvFile:
#        writer = csv.writer(csvFile, delimiter = ',',quotechar='\'')
#        writer.writerow([data])


    respXML = requests.get(url=BiharMasterDataXML)
    with open('BiharData.xml', 'wb') as f:
        f.write(respXML.content)
    
        
def parseXML (xmlFile):
    
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    name, pcap = [],[]
    
    name =  [item.find('company_name').text for item in root.findall('./records/item')]
    pcap1 = [item.find('paidup_capital').text for item in root.findall('./records/item')]
    pcap = list(map(int, pcap1))
    
    matrix = pd.DataFrame({'company_name':name, 'paidup_capital':pcap} )
    print (matrix)

    index = np.arange(len(name))
    

    plt.bar(index, pcap, align='center',alpha=0.5, color = "g")
    plt.ylabel('Paidup Capital', fontsize=20,  color='red')
    plt.xlabel('Company', fontsize=20,  color='red')
    plt.ticklabel_format(useOffset=False, style='plain')
    
 
    plt.xticks(index, name, fontsize=7, rotation=90)
    plt.show()
    

    

def main():
    loadData ()
    parseXML ('BiharData.xml')
    
    
if __name__ == "__main__":
    main()
    

