

class CDataNumber:
    strDataNumber = ""
    arrRedNumber = []
    nBlueNumber = -1

def getArrayDataNumberInfo():
    tFile = open("../DataNumber.txt", 'r')
    arrFileInfo = tFile.readlines()
    arrDataNumberList = []
    for strInfo in arrFileInfo:
        try:
            tDataNumber = CDataNumber()
            strDateNumber, strNumber = strInfo.split(":")
            arrNumber = strNumber.split(",")
            arrRedNumber = arrNumber[0:6]
            nBlueNumber = int(arrNumber[6])
            arrRedNumber = list(map(int, arrRedNumber))
            tDataNumber.strDataNumber = strDateNumber
            tDataNumber.arrRedNumber = arrRedNumber
            tDataNumber.nBlueNumber = nBlueNumber
            arrDataNumberList.append(tDataNumber)
        except:
            pass
    return arrDataNumberList

def getNumberPower(arrDataNumberList):
    nDateCount = len(arrDataNumberList)
    print(nDateCount)
    #双色球33个红色球 16个蓝色球
    #获取单个球在总的出现次数总的概率，红球总次数=期数*7， 篮球总次数=期数
    nRedDenominator = 7 * nDateCount
    nBlueDenominator= nDateCount
    arrRedNumberCount = [0] * 50
    arrBlueNumberCount = [0] * 30
    for tDataNumber in arrDataNumberList:
        for nNumber in tDataNumber.arrRedNumber:
            if(arrRedNumberCount[nNumber] == 0):
                arrRedNumberCount[nNumber] = 1
            else:
                arrRedNumberCount[nNumber] += 1
        nBlueNumber = tDataNumber.nBlueNumber
        if(arrBlueNumberCount[nBlueNumber] == 0):
            arrBlueNumberCount[nBlueNumber] = 1
        else:
            arrBlueNumberCount[nBlueNumber] += 1
    print(arrRedNumberCount)
    print(arrBlueNumberCount)
    for nIndex in range(0, len(arrRedNumberCount)):
        print("index;", nIndex, " ", arrRedNumberCount[nIndex], "power:", arrRedNumberCount[nIndex] / nRedDenominator)





if __name__ == '__main__':
    #获取信息列表
    arrDataNumberList = getArrayDataNumberInfo()
    print(arrDataNumberList)
    getNumberPower(arrDataNumberList)