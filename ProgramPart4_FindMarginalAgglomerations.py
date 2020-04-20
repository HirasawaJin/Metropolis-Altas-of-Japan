print("#####################\nPart 3 program START.\n#####################")

import metadata

def check_marginal_cell(Y_axis,X_axis):
    y = int(Y_axis)
    x = int(X_axis)
    
    if y ==0 and x == 0:
        parameter = (1,"upperleft_"+str(y)+"_"+str(x))

    # 1.2 upper right
    elif y ==0 and x == 319:
        parameter = (1,"upperright_"+str(y)+"_"+str(x))

    # 1.3 bottom left
    elif y ==319 and x == 0:
        parameter = (1,"bottomleft_"+str(y)+"_"+str(x))

    # 1.4 bottom right
    elif y ==319 and x == 319:
        parameter = (1,"bottomright_"+str(y)+"_"+str(x))

    # 2. edge
    # 2.1 top
    elif y ==0 and ( x !=0 and x !=319):
        parameter = (1,"top_"+str(y)+"_"+str(x))

    # 2.2 bottom
    elif y ==319 and ( x !=0 and x !=319):
        parameter = (1,"bottom_"+str(y)+"_"+str(x))

    # 2.3 left
    elif ( y !=0 and y != 319 ) and x == 0:
        parameter = (1,"left_"+str(y)+"_"+str(x))

    # 2.4 right
    elif ( y !=0 and y != 319 ) and x == 319:
        parameter = (1,"right_"+str(y)+"_"+str(x))
        
    else:
        parameter = (0,0)
        
    return parameter




if __name__ == "__main__":

    valid_Lv1meshID = metadata.call_populated_lv1mesh()

    MarginalAgglomerationsLIST = []

    for meshID in valid_Lv1meshID:
    #meshID = input("Please Enter a Valid Lv1 MeshID : ")
    
        RegionalAggloDATA = []
        with open("data/regional_agglomeration_data_sorted/population_rank_"+str(meshID)+".csv" , "r") as input_file:
            for line in input_file:
                NewLine = line.strip()
                NewLine = NewLine[:-1]
                NewLine = NewLine.strip().split(",")
                RegionalAggloDATA.append(NewLine)                
          
        ############################################
        ######## Marginal Agglomerations ###########
        ############################################
        
        buffer = []

        for EachAggloDATA in RegionalAggloDATA:
            
            RegionalAggloIDENTITY = str(meshID) +"_"+ str(EachAggloDATA[0])
            
            MarginalCellPosition = []
            OneMarginalAggloDATA = []
            
            # to obtain a pure list of cellID
            CellLIST = EachAggloDATA[2:]
            
            for EachCell in CellLIST:
            
                CellINFO = EachCell.split("_")

                cellY = int(CellINFO[1])
                cellX = int(CellINFO[2])
                
                parameter = check_marginal_cell(cellY,cellX)
                
                check,position = parameter
                
                ValueBuffer = position
                
                if check == 1:
                    MarginalCellPosition.append(ValueBuffer)
                
            if len(MarginalCellPosition) != 0:
                OneMarginalAggloDATA.append(RegionalAggloIDENTITY)
                OneMarginalAggloDATA = OneMarginalAggloDATA + MarginalCellPosition
                
                buffer = OneMarginalAggloDATA[:]
                MarginalAgglomerationsLIST.append(buffer)
                
            #print("RegionalAggloIDENTITY\t",RegionalAggloIDENTITY)
            #print(OneMarginalAggloDATA)
            #print(MarginalAgglomerationsLIST)

    with open("data/marginal_agglomeration_data/marginal_agglomerations"+".csv" , "w") as output_file:
        for each_row in MarginalAgglomerationsLIST:
            for each_field in each_row:
                output_file.write(str(each_field)+",")
            output_file.write("\n")

    print("Discovery in total " + str(len(MarginalAgglomerationsLIST)) + " of marginal agglomerations.")    
            
    print("#####################\nPart 3 program END. All agglomeration data is output.\n#####################")  