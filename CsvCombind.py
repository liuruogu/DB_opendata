__author__ = 'liu'
import pandas as pd
import io
import requests
import os

os.path.getsize()

# Load the data into dataframe
def LoadCsv(FileName):
    first = pd.read_csv(FileName)
    return first

# Combine two datafram together
def CombineCsv(FirstCsv,SecondCsv):

    frames = [FirstCsv,SecondCsv]
    CombinedCsv = pd.concat(frames)
    CombinedCsv.to_csv('first.csv', sep='\t', encoding='utf-8')
    return CombinedCsv

def main():
    # FirstCsv = LoadCsv('0002.csv')
    # SecondCsv = LoadCsv('0003.csv')
    # CombineCsv(FirstCsv,SecondCsv)

    # firstCsv = LoadCsv("first.csv")
    # for i in range(1,5):
    #     print(i)
    #     print("000"+i+".csv")
    #     firstCsv = LoadCsv("first.csv")
    #     # first = pd.read_csv("000"+i+".csv")
    #     CombineCsv(firstCsv,first)

    x = '00'
    y = '00'
    i = 0
    filename = None

    while i<=2:
        j=0
        while j<=9:
            k=0
            while k<6:
                l=0
                while l<10:
                    filename = str(int(x[0])+i) + str(int(x[1]) + j) + str(int(y[0])+k) + str(int(y[1]) + l)
                    print(filename)
                    # if filename != '0001':
                    url="https://trnet.cloudrail.jp/hackathon/self_train/0421/0/"+filename+".csv"
                    s=requests.get(url).content
                    c=pd.read_csv(io.StringIO(s.decode('utf-8')))
                    c.to_csv(filename+".csv", sep=',', encoding='utf-8')
                    # LoadCsv(c)
                    # CombineCsv(firstCsv,c)
                    l=l+1
                k=k+1
            j=j+1
            if filename == '2359':
                break
        i=i+1

    return

# call the main method
main()