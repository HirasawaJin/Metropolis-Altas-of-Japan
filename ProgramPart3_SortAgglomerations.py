print("#####################\nPart 3 program START.\n#####################")

import metadata

if __name__ == "__main__":

    valid_Lv1meshID = metadata.call_populated_lv1mesh()

    for meshID in valid_Lv1meshID:
    #meshID = input("Please Enter a Valid Lv1 MeshID : ")
    
        RegionalAggloDATA = []
    
        with open("data/regional_agglomeration_data/agglomeration_"+str(meshID)+".csv" , "r") as input_file:
            for line in input_file:
                NewLine = line.strip()
                NewLine = NewLine[:-1]
                NewLine = NewLine.strip().split(",")
                RegionalAggloDATA.append(NewLine)
                
        meshDATA = []
        
        for RegionalAgglo in RegionalAggloDATA:
        
            RegionalAggloPopulation = 0
            RegionalAggloNewLIST = []
            
            for CellID in RegionalAgglo:
            
                CellINFO = CellID.split("_")
                
                meshID = int(CellINFO[0])
                cellY = int(CellINFO[1])
                cellX = int(CellINFO[2])
                cellPopulation = int(CellINFO[3])
                
                RegionalAggloPopulation += cellPopulation
                
                buffer = CellID
                RegionalAggloNewLIST.append(buffer)
            
            RegionalAggloNewLIST.insert(0,RegionalAggloPopulation)
            meshDATA.append(RegionalAggloNewLIST)
        
        meshDATA.sort(reverse=True)
        
        for index in range(len(meshDATA)):
            meshDATA[index].insert(0,index)        
  
        with open("data/regional_agglomeration_data_sorted/population_rank_"+str(meshID)+".csv" , "w") as output_file:
            for each_row in meshDATA:
                for each_field in each_row:
                    output_file.write(str(each_field)+",")
                output_file.write("\n")
            
    print("#####################\nPart 3 program END. All agglomeration data is output.\n#####################")  