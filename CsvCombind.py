__author__ = 'liu'
import pandas as pd
import io
import requests


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
    FirstCsv = 'first.csv'
    firstCsv = LoadCsv(FirstCsv)

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
                    if filename != '0001':
                        url="https://trnet.cloudrail.jp/hackathon/self_train/0420/0/"+filename+".csv"
                        s=requests.get(url).content
                        c=pd.read_csv(io.StringIO(s.decode('utf-8')))
                        c.to_csv(filename+".csv", sep='\t', encoding='utf-8')
                        CombineCsv(firstCsv,c)
                    l=l+1
                k=k+1
            j=j+1
            if filename == '2359':
                break
        i=i+1

    return

# call the main method
main()