print("#####################\nPart 8.5 program START.\n#####################")

def find_deltainlist(listname):
    listname.sort()
    smallestnumber = int(listname[0])
    listname.sort(reverse=True)
    largestnumber = int(listname[0])
    
    delta = abs(smallestnumber - largestnumber)
    return delta
    
def trim_validlist(listname):
    qR = 0
    

import metadata
from PIL import Image, ImageDraw
import numpy

valid_Lv1meshID = metadata.call_populated_lv1mesh()

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
              
            tempMeshIDY = set()
            tempMeshIDX = set()                
            for items in QuestedGlobalAggloMesh:
                Y = int(items[:2])
                tempMeshIDY.add(Y)
                X = int(items[2:])
                tempMeshIDX.add(X)
            MeshIDY = []
            MeshIDX = []
            for items in tempMeshIDY:
                MeshIDY.append(items)
            for items in tempMeshIDX:
                MeshIDX.append(items)                
            MeshHeight = find_deltainlist(MeshIDY) + 1 
            MeshWidth = find_deltainlist(MeshIDX) + 1
            matrix = [[0 for i in range(320*MeshWidth)] for j in range(320*MeshHeight)]
            MeshIDY.sort(reverse=True)
            MeshIDX.sort()             
            # so we created a matrix that is big enough
            # lets pour all data into it           
            
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
                
                OffsetY = abs(int(MeshIDY[0]) - int(meshID[:2]))
                OffsetX = abs(int(meshID[2:]) - int(MeshIDX[0]))
                
                for eachAggloDATA in NeededDATA:
                    cellDATAs = eachAggloDATA[2:]
                    
                    for eachCell in cellDATAs:
                        CellINFO = eachCell.split("_")
                        meshID = int(CellINFO[0])
                        cellY = int(CellINFO[1]) + 320*OffsetY
                        cellX = int(CellINFO[2]) + 320*OffsetX
                        cellPopulation = int(CellINFO[3])    
                        
                        matrix[cellY][cellX] = cellPopulation
                        CellsCount += 1


            # First trim height
            Ysumpop = []
            for rows in matrix:
                rowpop = sum(rows)
                Ysumpop.append(rowpop)
            #Ysumpop = [0,0,0,0,123,1515,6367,52,12,0,0,0,0]
            YLeadingZero = 0
            YFollowingZero = 0            
            stopper = -1
            n = 0
            while stopper != 1:
                if Ysumpop[n] == 0:
                    n += 1                
                elif Ysumpop[n] != 0:
                    stopper = 1
                    YLeadingZero = n
            stopper = -1
            n = -1
            while stopper != 1:
                if Ysumpop[n] == 0:
                    n -= 1                
                elif Ysumpop[n] != 0:
                    stopper = 1
                    YFollowingZero = n
            
            trimedmatrix = matrix[YLeadingZero+1:YFollowingZero+1]
            
            # Second trim width
            XLeadingZero = []
            XFollowingZero = []
            
            for (y,rows) in enumerate(trimedmatrix):
                stopper = -1
                n = 0
                while stopper != 1:
                    if rows[n] == 0:
                        n += 1                
                    elif rows[n] != 0:
                        stopper = 1
                        tempnum = n
                        XLeadingZero.append(tempnum)
                stopper = -1
                n = -1
                while stopper != 1:
                    if rows[n] == 0:
                        n -= 1                
                    elif rows[n] != 0:
                        stopper = 1
                        tempnum = n
                        XFollowingZero.append(tempnum)           
            for y in range(len(trimedmatrix)):
                trimedmatrix[y] = trimedmatrix[y][min(XLeadingZero)+1:max(XFollowingZero)+1]
                
            filename = "GlobalAggloID_" + str(GlobalAggloID)
            
            with open("data/global_agglomeration_map/"+str(filename)+".csv" , "w") as output_file:
                for each_row in trimedmatrix:
                    for each_field in each_row:
                        output_file.write(str(each_field)+",")
                    output_file.write("\n")


            g = open("data/global_agglomeration_map/"+str(filename)+".csv" , "r")
            #temp = numpy.genfromtxt(g, delimiter = ',', autostrip=True,)
            temp = numpy.array(trimedmatrix)
            im = Image.fromarray(temp,"RGB")
            pix = im.load()
            #rows, cols = im.size
            height = len(trimedmatrix)
            width = len(trimedmatrix[0])
            for x in range(width):
                for y in range(height):
                    #print(str(x) + " " + str(y))
                    
                    if temp[y,x] == 0:
                        pix[x,y] = (256,256,256)
                    else:                    
                        pix[x,y] = (int(round(256 - (256)/(1+7*2.718281828**(-(0.065*(temp[y,x]/(10000/256))))))),
                                    int(round(256 - (256)/(1+7*2.718281828**(-(0.065*(temp[y,x]/(10000/256))))))),
                                    int(round(256 - (256)/(1+7*2.718281828**(-(0.065*(temp[y,x]/(10000/256))))))))
                    # (R,G,B)
                    #要用顏色深淺黎表達人口密度
                    #人口密度上限係10000
                    #先將10000除256 得出256階linear色階
                    #然後用f(x)=(256)/(1+7e^(-(b*x)))
                    #用病毒傳播嘅數學模型黎分配新嘅色階
                    #輸入linear色階
                    #得出新嘅logistic色階

            im.save("data/global_agglomeration_map/"+str(filename) + '.tif')
            print("This Agglomeration has an area of", str(CellsCount), "cells.\n",
                    "Around", CellsCount*(1/16) ,"sq.km .")        
            print("Map is output")


        elif query == "quit":
            break




    print("#####################\nPart 8.5 program END.\n#####################")

