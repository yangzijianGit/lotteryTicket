import urllib.request
import ssl
import urllib.parse
import gzip
import os

ssl._create_default_https_context = ssl._create_unverified_context


def ungzip(data):
    try:
        data = gzip.decompress(data)
    except:
        pass
    return data


def decodeUtf(data):
	try:
		data = data.decode('utf-8')
	except:
		pass
	return data

def getBallNumber(data):
	strInfo = str(data)

	def getSplitNum(strFind, nIndex):
		nBeginIndex = strInfo.find(strFind, nIndex) + len(strFind)
		nEndIndex = strInfo.find('<', nBeginIndex)
		strNumber = strInfo[nBeginIndex: nEndIndex]
		#print("nBeginIndex:", nBeginIndex, " nEndIndex:", nEndIndex)
		#print(strNumber)
		return nEndIndex, strNumber

	strRedFind = 'class=\"ball_red\">'
	strBlueFind = 'class=\"ball_blue\">'
	nRedIndex = 0
	redBall=set()
	for i in range(0, 6):
		nRedIndex, strNumber = getSplitNum(strRedFind, nRedIndex)
		redBall.add(int(strNumber))
	nBlueIndex, strNumber = getSplitNum(strBlueFind, 0)
	return redBall, int(strNumber)

def getUrlInfo(dataNumber):
	redBall = set()
	nBlueBall = 0
	try:
		url = str("https://kaijiang.500.com/shtml/ssq/") + str(dataNumber) + str(".shtml")
		print(url)
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
		}
		req = urllib.request.Request(url, headers=headers)
		resp = urllib.request.urlopen(req)
		data = decodeUtf(ungzip(resp.read()))
		#print(data)
		redBall, nBlueBall = getBallNumber(data)
		#print("redBall:", redBall, " nBlueBall:", nBlueBall)
	except:
		pass
	return redBall, nBlueBall

if __name__ == '__main__':
	tFile = open("../DataNumber.txt", "w")
	for dataNumber in range(19000, 19147):
		redBall, nBlueBall = getUrlInfo(dataNumber)
		strNumber = ""
		for redNumber in redBall:
			strNumber = strNumber + str(redNumber) + str(",")
		strNumber = strNumber + str(nBlueBall)
		tFile.write(str(dataNumber) + ":" + strNumber)
		tFile.write('\n')
	tFile.close()
