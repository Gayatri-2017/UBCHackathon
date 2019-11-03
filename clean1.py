import csv
#import sys
#fil = sys.argv[1]
fil = "/Users/apple/Desktop/UBCHackathon/ubc_course_calendar_data_copy.csv"
with open(fil) as f:
    reader = csv.reader(f)
    for i in reader:
        l = []
        for x in i:
            if ';'  in x:
                m = x.split(';')
                l.append(m)
            else:
                l.append(x)

#        for j in l[2]:
#            print(l[0]+','+l[1]+','+j)
#        j1 = ''
#        print(list(l[19]))
        ins_str = ''
        if (type(l[19]) == str):
#                ins_str = ','.join(l[:19])+ ',' + ','.join(l[20:])
                print(l[0]+','+l[1]+','+ l[19])
#                print(ins_str)
        elif (type(l[19]) == list):
#            ins_str = ','.join(l[:19])+','
            for j in l[19]:    
                
#                ins_str += ','+j + ','.join(l[20:])
                print(l[0]+','+l[1]+','+ j)
            
#                print(ins_str)