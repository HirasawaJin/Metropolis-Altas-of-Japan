print("#####################\nPart 6 program START.\n#####################")

import metadata

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

if __name__ == "__main__":

    AdjcentAgglomerationsLIST = []

    with open("data/adjcent_agglomeration_data/adjcent_agglomerations"+".csv" , "r") as input_file:
        for line in input_file:
            NewLine = line.strip()
            NewLine = NewLine[:-1]
            NewLine = NewLine.strip().split(",")
            AdjcentAgglomerationsLIST.append(NewLine)

    # Founding LCM Least Commom Multiple

    #GlobalAggloID = [1,["A","B"],["A","B"],[0]] # for testing
    #AdjcAggloLIST = [ ["A","B"],["B","C"],["C","D"],["E","F"]] # for testing

    AdjcAggloLIST = AdjcentAgglomerationsLIST[:]

    GlobalAggloIDFullLIST = []
    for (AdjcAggloID,Elements) in enumerate(AdjcAggloLIST):

        a = AdjcAggloID+1
        
        B = set(Elements)
            
        D = {AdjcAggloID}

        GlobalAggloID = []
        GlobalAggloID.append(a)
        GlobalAggloID.append(B)
        GlobalAggloID.append(D)
        GlobalAggloIDFullLIST.append(GlobalAggloID)

    CompletedGlobalAggloIDCheckLIST = set()


    while len(CompletedGlobalAggloIDCheckLIST) != len(GlobalAggloIDFullLIST):

        for (GlobalAggloIDINDEX,GlobalAggloID) in enumerate(GlobalAggloIDFullLIST):
            
            #print(1,GlobalAggloID)
            #print(2,CompletedGlobalAggloIDCheckLIST)
            #print(3,check_validity(GlobalAggloID,CompletedGlobalAggloIDCheckLIST))
            
            GlobalAggloIDIdentityCode = GlobalAggloIDFullLIST[GlobalAggloIDINDEX][0]

            if (GlobalAggloIDIdentityCode in CompletedGlobalAggloIDCheckLIST) == False:
            # skip scannig completed rows
                
                for (AdjcAggloINDEX,AdjcAggloSET) in enumerate(AdjcAggloLIST):
                
                    AdjcAggloIDIdentityCode = AdjcAggloINDEX
                    AdjcAggloSET = AdjcAggloSET
                    
                    ValidityChecker = 0
                    for item in AdjcAggloSET:
                        if (item in GlobalAggloIDFullLIST[GlobalAggloIDINDEX][1]) == True:
                            ValidityChecker += 1
                    
                    if ValidityChecker != 0:
                    # if it contains any of the existing elements, it has a relationship with this GlobalAggloID
                    
                        #print(6,TheElement)
                        #print(7,AdjcAggloSET)
                        #print(8,check_validity(TheElement,AdjcAggloSET))
                        #print(9,check_validity2(ValidityChecker))
                        #print(10,[AdjcAggloID])                                        
                        #print(11,TheAdjcAggloID)
                        #print(12,GlobalAggloID[3])
                        #print(13,check_validity(TheAdjcAggloID,GlobalAggloID[3]))
                            
                        if (AdjcAggloIDIdentityCode in GlobalAggloIDFullLIST[GlobalAggloIDINDEX][2]) == False:
                        # if it is not dulipcate, we can grab new elements
                        
                            for EachElement in AdjcAggloSET:                                 
                                NewElementToAdd = EachElement
                                GlobalAggloIDFullLIST[GlobalAggloIDINDEX][1].add(NewElementToAdd)
                                
                            GlobalAggloIDFullLIST[GlobalAggloIDINDEX][2].add(AdjcAggloINDEX)
                            #print(16,AdjcAggloID)
                            #print(17,GlobalAggloID[3])
                            
                            # Algoritm complete. All we need to do is to check wether there is missing part.        
                RowsWeNeed = set()
                for (AdjcAggloID,AdjcAggloSET) in enumerate(AdjcAggloLIST):
                    ValidityChecker = 0
                    for item in AdjcAggloSET:
                        if (item in GlobalAggloIDFullLIST[GlobalAggloIDINDEX][1]) == True:
                            ValidityChecker += 1
                    if ValidityChecker != 0:
                        RowsWeNeed.add(AdjcAggloID)
                        
                #print(RowsWeNeed)    
                #print(GlobalAggloID[3])
                #print(len(RowsWeNeed))
                #print(len(GlobalAggloID[3]))
                
                Score = 0
                if len(RowsWeNeed) == len(GlobalAggloIDFullLIST[GlobalAggloIDINDEX][2]):
                    Score += 1
                #else:
                    #print("Something wrong.")
                    
                if RowsWeNeed == GlobalAggloIDFullLIST[GlobalAggloIDINDEX][2]:
                    Score += 1
                #else:
                    #print("This is totally wrong!!!")
                #print("id=",GlobalAggloIDFullLIST[GlobalAggloIDINDEX][0],"Score=",Score)
                if Score == 2:
                    if (GlobalAggloIDIdentityCode in CompletedGlobalAggloIDCheckLIST) == False:
                        CompletedGlobalAggloIDCheckLIST.add(GlobalAggloIDIdentityCode)
                        
            #print(len(CompletedGlobalAggloIDCheckLIST))

    #print(len(CompletedGlobalAggloIDCheckLIST))
    #print(len(GlobalAggloIDFullLIST))
    with open("data/global_agglomeration_data/global_agglomerations_beta"+".csv" , "w") as output_file:
        for each_row in GlobalAggloIDFullLIST:
            for each_field in each_row:
                output_file.write(str(each_field)+",")
            output_file.write("\n")
            
    print("Part6.1 is finished.") 

    FinalGlobalAggloIDFullLIST = []
    
    for TotalNumberOfGlobalAgglo in range(len(GlobalAggloIDFullLIST)):        
        GlobalAggloINFO = GlobalAggloIDFullLIST[TotalNumberOfGlobalAgglo][1]
        if (GlobalAggloINFO in FinalGlobalAggloIDFullLIST) == False:
            FinalGlobalAggloIDFullLIST.append(GlobalAggloINFO)

    with open("data/global_agglomeration_data/global_agglomerations_final"+".csv" , "w") as output_file:
        for each_row in FinalGlobalAggloIDFullLIST:
            for each_field in each_row:
                output_file.write(str(each_field)+",")
            output_file.write("\n")

    print("#####################\nPart 6 program END. Global Agglomerations Fulllist is output.\n#####################")

