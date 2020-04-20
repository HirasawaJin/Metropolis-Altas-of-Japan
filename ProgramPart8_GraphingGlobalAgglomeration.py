print("#####################\nPart 8 program START.\n#####################")

import metadata
from PIL import Image, ImageDraw
from numpy import genfromtxt

valid_Lv1meshID = metadata.call_populated_lv1mesh()

def check_validity(targetlist,check_from):

    checkkkresult = []

    for (i,target) in enumerate(targetlist):
        if check_from.count(target) > 0 : # if list_check_from contains target, we made it!
            checkkkresult.append([target,1])
        else:
            checkkkresult.append([target,0])
    #print(result)
    return checkkkresult

def check_validity2(result):
    # this function is used to check
    # whether one list contain element on another list
    # this is use after check_validity
    # as the result of previous function = [ [a,0],[b,1],[c,1] ]
    # it is more convient to have a function to check whether "1" == result[n][1]

    ValidiyCodeOfResult = []

    for (i,EachSET) in enumerate(result):
        ValidiyCodeOfResult.append(EachSET[1])
        # so we obtain ValidiyCodeOfResult = [1,1,0,0,1]
        # all we need is to count 1 in this list
    if ValidiyCodeOfResult.count(1) == 0:
        return 0 # means there is no "1"
    else:
        return 1 # means there has "1"

def new_dictionary(meshid):
    key = str(meshid)
    value = []
    dictionary = {key:value}
    return dictionary


if __name__ == "__main__":

    while True:
        query = input("Please input the Global Agglomeration's ID the you are interested in : ")
        
        if query != "quit":
        
            GlobalAggloID = int(query)
            
            bigpicture = []
            with open("data/big_picture/bigpicture.csv" , "r") as input_file:
                for line in input_file:
                    NewLine = line.strip()
                    NewLine = NewLine[:-1]
                    NewLine = NewLine.strip().split(",")
                    bigpicture.append(NewLine)

            QuestedGlobalAggloINFO = bigpicture[GlobalAggloID]
            
            QuestedGlobalAggloPopulation = QuestedGlobalAggloINFO[1]
            
            QuestedGlobalAggloMesh = set()
            
            for length in range(len(QuestedGlobalAggloINFO)-2):
                QuestedGlobalAggloMesh.add(QuestedGlobalAggloINFO[length+2][:4])
            
            print("Global Agglomeration you selected is located in mesh\n",
                    QuestedGlobalAggloMesh ,"\n",
                    "with total population of", int(QuestedGlobalAggloPopulation),".")

            QuestedGlobalAggloINFO = QuestedGlobalAggloINFO[2:]
            
            MeshIDs = []
            
            for items in QuestedGlobalAggloMesh:
                MeshIDs.append([items])
            
            for element in QuestedGlobalAggloINFO:
                for (index,everyMeshID) in enumerate(MeshIDs):
                    if str(everyMeshID[0]) == str(element[:4]):
                        newAggloID = element[5:element.index("_",5)]
                        MeshIDs[index].append(newAggloID)
            
            # MeshIDs = [ [ meshID_1, AggloID, AggloID, AggloID ],
            #             [ meshID_2, AggloID, AggloID, AggloID ],
            #             [ meshID_3, AggloID, AggloID, AggloID ] ]
            
            CellsCount = 0
            
            for eachMeshDATAs in MeshIDs:
                
                meshID = eachMeshDATAs[0]
                AggloIDS = eachMeshDATAs[1:]

                RegionalAggloDATAs = []
                
                with open("data/regional_agglomeration_data_sorted/population_rank_"+str(meshID)+".csv" , "r") as input_file:
                    for line in input_file:
                        NewLine = line.strip()
                        NewLine = NewLine[:-1]
                        NewLine = NewLine.strip().split(",")
                        RegionalAggloDATAs.append(NewLine)
              
                NeededDATA = []
                
                for eachAggloID in AggloIDS:
                    buffer = RegionalAggloDATAs[int(eachAggloID)]
                    NeededDATA.append(buffer)
                
                # NeededDATA = [ [ AggloID_1, cellID, cellID, cellID ],
                #                [ AggloID_2, cellID, cellID, cellID ],
                #                [ AggloID_3, cellID, cellID, cellID ] ]
                
                matrix = [[0 for i in range(320)] for j in range(320)]

                for eachAggloDATA in NeededDATA:
                    cellDATAs = eachAggloDATA[2:]
                    
                    for eachCell in cellDATAs:
                        CellINFO = eachCell.split("_")
                        meshID = int(CellINFO[0])
                        cellY = int(CellINFO[1])
                        cellX = int(CellINFO[2])
                        cellPopulation = int(CellINFO[3])    
                        
                        matrix[cellY][cellX] = cellPopulation
                        CellsCount += 1

                filename = str(GlobalAggloID)+"_"+str(meshID)
                
                with open("data/map/"+str(filename)+".csv" , "w") as output_file:
                    for each_row in matrix:
                        for each_field in each_row:
                            output_file.write(str(each_field)+",")
                        output_file.write("\n")


                g = open("data/map/"+str(filename)+".csv" , "r")
                temp = genfromtxt(g, delimiter = ',')
                #temp = matrix
                im = Image.fromarray(temp).convert('RGB')
                pix = im.load()
                rows, cols = im.size
                for x in range(320):
                    for y in range(320):
                        #print(str(x) + " " + str(y))
                        pix[x,y] = (int(temp[y,x] // 256 // 256 % 256),
                                    int(temp[y,x] // 256  % 256),
                                    int(temp[y,x] % 256))
                im.save(g.name[0:-4] + '.tif')
            print("This Agglomeration has an area of", str(CellsCount), "cells.\n",
                    "Around", CellsCount*(1/16) ,"sq.km .")        
            print("Maps are output")
        
        elif query == "quit":
            break




    print("#####################\nPart 8 program END. Big Picture is output.\n#####################")
