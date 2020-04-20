print("#####################\nPart 6.5 program START.\n#####################")

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

    GlobalAggloIDFullLIST = []

    with open("data/global_agglomeration_data/global_agglomerations_final"+".csv" , "r") as input_file:
        for line in input_file:
            NewLine = line.strip()
            NewLine = NewLine[:-1]
            NewLine = NewLine.strip().split(",")
            GlobalAggloIDFullLIST.append(NewLine)

    for (index,EachGlobalAgglo) in enumerate(GlobalAggloIDFullLIST):
    
        TotalPopulation = 0
        
        for EachRegionalAgglo in EachGlobalAgglo:            
            meshID = int(EachRegionalAgglo[:4])
            AggloID = int(EachRegionalAgglo[5:])
            
            temp_list = []
            with open("data/regional_agglomeration_data_sorted/population_rank_"+str(meshID)+".csv" , "r") as input_file2:
                for line in input_file2:
                    NewLine = line.strip()
                    NewLine = NewLine[:-1]
                    NewLine = NewLine.strip().split(",")
                    temp_list.append(NewLine)
            
            
            TotalPopulation += int(temp_list[AggloID][1])
        
        GlobalAggloIDFullLIST[index].insert(0,TotalPopulation)
        
    GlobalAggloIDFullLIST.sort(reverse=True)
    

    with open("data/global_agglomeration_data/global_agglomerations_finalsorted"+".csv" , "w") as output_file:
        for each_row in GlobalAggloIDFullLIST:
            for each_field in each_row:
                output_file.write(str(each_field)+",")
            output_file.write("\n")

    print("#####################\nPart 6.5 program END. Global Agglomerations Fulllist is output.\n#####################")

