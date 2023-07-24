#Este import nos permite leer archivos csv
import csv 

def read_csv(filename):
    with open(filename,'r') as file:
        reader = csv.reader(file,delimiter=',')
        header = next(reader)
        print(header)
        data=[]
        for row in reader:
            iterable=list(zip(header,row))
            #zip nos permite unir dos listas en una sola
            country_dict={key:value for key,value in iterable}

            data.append(country_dict)
            print(country_dict)
        return data
if __name__ == '__main__':
    data=read_csv('./APP/data.csv')
    print('**********')
    print(data[0])