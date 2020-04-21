
rows = []
for u in range(8):
    for i in range(10):
        for o in range(2):
            for p in range(2):
                fields = []
                for q in range(8):
                    for w in range(10):
                        for e in range(2):
                            for r in range(2):
                                                              
                                id = 709033 + 10000*q + 100*w + 10*e + 1*r -2*p -20*o -1000*i - 100000*u

                                if (10000<= int(id)) and  (int(id)<=99999): 
                                    id = "0"+str(id)
                                elif (1000<= int(id)) and  (int(id)<=9999): 
                                    id = "00"+str(id)
                                elif (100<= int(id)) and  (int(id)<=999): 
                                    id = "000"+str(id)
                                elif (10<= int(id)) and  (int(id)<=99): 
                                    id = "0000"+str(id)
                                elif (1<= int(id)) and  (int(id)<=9): 
                                    id = "00000"+str(id)
                                elif 0 == int(id): 
                                    id = "0000000"+str(id)
                                
                                fields.append(str(id))
                rows.append(fields)

meshIDconverter = rows[:]

with open("data/meshIDconverter.csv" , "w") as output_file:
    for each_row in meshIDconverter:
        for each_field in each_row:
            output_file.write(str(each_field)+",")
        output_file.write("\n")
