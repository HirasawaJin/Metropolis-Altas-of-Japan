print("#####################\nPart 9 program START.\n#####################")

import metadata

valid_Lv1meshID = metadata.call_populated_lv1mesh()

if __name__ == "__main__":

    while True:
        query = input("Please input the Global Agglomeration's ID the you are interested in : ")
        
        if query != "quit":
        
            GlobalAggloID = int(query)
            
            
            
            
            meshIDconverter = []
            with open("data/meshIDconverter.csv" , "r") as input_file:
                for line in input_file:
                    NewLine = line.strip()
                    NewLine = NewLine[:-1]
                    NewLine = NewLine.strip().split(",")
                    meshIDconverter.append(NewLine)    
            
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
            
                CoordinateOfGlobalAgglo=[]
                
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

                for eachAggloDATA in NeededDATA:
                    cellDATAs = eachAggloDATA[2:]
                    
                    for eachCell in cellDATAs:
                        
                        #MeshY = 68-int(meshID[:2])
                        #MeshX = int(meshID[3:])-22
                        CellINFO = eachCell.split("_")
                        CellY = int(CellINFO[1])
                        CellX = int(CellINFO[2])
                        CellPop = int(CellINFO[3])    

                        #Y_axis = 46 - (MeshY+CellY/320)*(2/3)
                        #X_axis = 122 + (MeshX + CellX/320)
                        
                        prefix = str(meshID)
                        supfix = str(meshIDconverter[CellY][CellX])
                        keycode = prefix+supfix
                        
                        CoordinateOfGlobalAgglo.append([keycode,CellPop])
                        CellsCount += 1

                CoordinateOfGlobalAgglo.insert(0,["KEY_CODE","Population"])

                filename = str(GlobalAggloID)+"_"+str(meshID)
                with open("data/coordinate/coordinate_"+str(filename)+".csv" , "w") as output_file:
                    for each_row in CoordinateOfGlobalAgglo:
                        for each_field in each_row:
                            output_file.write(str(each_field)+",")
                        output_file.write("\n")
                        
            print("This Agglomeration has an area of", str(CellsCount), "cells.\n",
                    "Around", CellsCount*(1/16) ,"sq.km .") 
            print("#####################\nCoordinate is output\n#####################")
        
        elif query == "quit":
            break




    print("#####################\nPart 9 program END. Coordinate is output.\n#####################")

