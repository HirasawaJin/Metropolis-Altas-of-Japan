print("#####################\nPart 7 program START.\n#####################")

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

    regional_agglomerations_fulllist = []

    # now checking on agglomeration
    # obtain the list of meshID
    for meshID in valid_Lv1meshID:

        OriginalRegionalAggloDATAs = []
        # start inputing files
        with open("data/regional_agglomeration_data_sorted/population_rank_"+str(meshID)+".csv" , "r") as input_file:
            for line in input_file:
                NewLine = line.strip()
                NewLine = NewLine[:-1]
                NewLine = NewLine.strip().split(",")
                OriginalRegionalAggloDATAs.append(NewLine)

        # first extract data of each agglomeration

        CopyOfRegionalAggloDATAs = OriginalRegionalAggloDATAs[:]

        NewRegAggloINFO = []

        for (RegionalAggloINDEX,RegionalAggloDATA) in enumerate(OriginalRegionalAggloDATAs):

            RegionalAggloINFO = []

            ######################################################################
            # Append the RegionalAggloID into RegionalAggloINFO                  #
            ###### START #########################################################
            RegionalAggloID = str(meshID) + "_" + str(OriginalRegionalAggloDATAs[RegionalAggloINDEX][0])
            # RegionalAggloINFO = [ RegionalAggloID, TotalPopulation, CellID, CellID, ... ]
            FirstElement = RegionalAggloID
            RegionalAggloINFO.append(FirstElement)
            ###### END ######

            ######################################################################
            # Append the TotalPopulation into RegionalAggloINFO                  #
            ###### START #########################################################
            RegionalAggloPopulation = OriginalRegionalAggloDATAs[RegionalAggloINDEX][1]
            SecondElement = RegionalAggloPopulation
            RegionalAggloINFO.append(SecondElement)
            #print(TotalPopulation)
            ###### END ######

            ######################################################################
            # Append CellID into RegionalAggloINFO                               #
            ###### START #########################################################
            # CellID = MeshID_Status_Y_X_Population
            CellDATAs = OriginalRegionalAggloDATAs[RegionalAggloINDEX][2:]
            RegionalAggloINFO = RegionalAggloINFO + CellDATAs
            ###### END ######

            ######################################################################
            # Append RegionalAggloID into FullLIST                               #
            ###### START #########################################################
            buffer = RegionalAggloINFO[:]

            NewRegAggloINFO.append(buffer)
            #print(RegionalAggloINFO)
            ###### END ######

        temp_buffer = NewRegAggloINFO[:]
        regional_agglomerations_fulllist = regional_agglomerations_fulllist + temp_buffer
    #print(regional_agglomerations_fulllist)

    #with open("data/big_picture/regional_agglomerations_fulllist"+".csv" , "w") as output_file:
        #for each_row in regional_agglomerations_fulllist:
            #for each_field in each_row:
                #output_file.write(str(each_field)+",")
            #output_file.write("\n")


    RegAggloIDFullLIST = regional_agglomerations_fulllist[:]

    FinalGlobalAggloIDFullLIST = []

    # start inputing files
    with open("data/global_agglomeration_data/global_agglomerations_final.csv" , "r") as input_file:
        for line in input_file:
            NewLine = line.strip()
            NewLine = NewLine[:-1]
            NewLine = NewLine.strip().split(",")
            FinalGlobalAggloIDFullLIST.append(NewLine)


    ######################################################################
    # BigPicture = [[GlobalAggloINFO], [GlobalAggloINFO]]                #
    ###### START #########################################################

    BigPicture = []

    AddedRegAgglo = set()

    for (LevelOneIDINDEX,LevelOneScan) in enumerate(RegAggloIDFullLIST):
    # call RegAggloFullLIST, to see whether a RegAgglo is actually a subset of GlobalAgglo
        if (LevelOneIDINDEX in AddedRegAgglo) == False:
            GlobalAggloINFO = []
            IfIsASubsetOfGlobal = []
            ThisIsASubsetOfGlobal = []
            for (LevelTwoIDINDEX,LevelTwoScan) in enumerate(FinalGlobalAggloIDFullLIST):
            # call FinalGlobalAggloIDFullLIST, scan for the identitical item.
                if LevelTwoScan.count(LevelOneScan[0]) > 0:
                # if any of the element inside GlobalAggloID == RegAggloID, this case need an special manipulation
                    IfIsASubsetOfGlobal.append(1)
                    for f in range(len(LevelTwoScan)):
                        CheckThisOut = LevelTwoScan[f]
                        ThisIsASubsetOfGlobal.append(CheckThisOut)

                elif LevelTwoScan.count(LevelOneScan[0])  == 0:
                # if all element inside GlobalAggloID != RegAggloID, this is an alone RegAgglo
                    IfIsASubsetOfGlobal.append(0)

            TotalPopulation = 0

            if IfIsASubsetOfGlobal.count(1) == 0:

            # if this is an allone RegAgglo, just simply append it to list
                ######################################################################
                # GlobalAggloEle = [RegionalAggloINFO, RegionalAggloINFO]        #
                ###### START #########################################################
                GlobalAggloEle = []
                ######################################################################
                # RegionalAggloINFO = RegAggloID_RegAggloPOP   #
                ######################################################################

                RegAggloID = RegAggloIDFullLIST[LevelOneIDINDEX][0]
                RegAggloPOP = RegAggloIDFullLIST[LevelOneIDINDEX][1]
                TotalPopulation += int(RegAggloIDFullLIST[LevelOneIDINDEX][1])
                RegionalAggloINFO = str(RegAggloID)+"_"+str(RegAggloPOP)
                GlobalAggloEle.append(RegionalAggloINFO)

                AddedRegAgglo.add(LevelOneIDINDEX)
                
                GlobalAggloINFO = GlobalAggloINFO + GlobalAggloEle
                ###### END ##########################################################


            elif IfIsASubsetOfGlobal.count(1) > 0:
                GlobalAggloEle = []
                for ThisGloAggloEle in ThisIsASubsetOfGlobal:

                    for (pretargetRegAggloIDINDEX,pretargetRegAggloINFO) in enumerate(RegAggloIDFullLIST):

                        if ThisGloAggloEle == pretargetRegAggloINFO[0]:
                            #print("Current:",pretargetRegAggloIDINDEX,pretargetRegAggloINFO)
                            ######################################################################
                            # GlobalAggloEle = [RegionalAggloINFO, RegionalAggloINFO]        #
                            ###### START #########################################################

                            ######################################################################
                            # RegionalAggloINFO = RegAggloID_RegAggloPOP   #
                            ###### START #########################################################
                            RegAggloID = pretargetRegAggloINFO[0]
                            RegAggloPOP = pretargetRegAggloINFO[1]
                            TotalPopulation += int(pretargetRegAggloINFO[1])
                            RegionalAggloINFO = str(RegAggloID)+"_"+str(RegAggloPOP)
                            ThisID = pretargetRegAggloIDINDEX
                            AddedRegAgglo.add(ThisID)
                    ###### END ##########################################################
                    GlobalAggloEle.append(RegionalAggloINFO)

                GlobalAggloINFO = GlobalAggloINFO + GlobalAggloEle
                ###### END ##########################################################


            ######################################################################
            # GlobalAggloPOP                                                     #
            ###### START #########################################################
            GlobalAggloINFO.insert(0,TotalPopulation)
            ###### END ##########################################################

            ######################################################################
            # BigPicture = [[GlobalAggloINFO], [GlobalAggloINFO]]                #
            ###### START #########################################################
            BigPicture.append(GlobalAggloINFO)
            ###### END ##########################################################

    BigPicture.sort(reverse=True)

    for (NumOfGlobalAgglo,NumOfGlobalAggloINFO) in enumerate(BigPicture):
        ID = NumOfGlobalAgglo
        BigPicture[NumOfGlobalAgglo].insert(0,ID)

    with open("data/big_picture/bigpicture"+".csv" , "w") as output_file:
        for each_row in BigPicture:
            for each_field in each_row:
                output_file.write(str(each_field)+",")
            output_file.write("\n")



    print("#####################\nPart 7 program END. Big Picture is output.\n#####################")
