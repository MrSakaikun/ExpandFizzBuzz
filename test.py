
def main():
    #ファイル名指定
    fileName = 'input.txt'
    #準備
    fizzbuzzDict = dict()
    number = 0
    #ファイル読み込み
    with open(fileName,'r') as f:
        for line in f:
            if ':' in line:
                keyValue = line.split(':')
                fizzbuzzDict[int(keyValue[0])] = keyValue[1].rstrip('\n')
            else:
                number = int(line)
                break

    #昇順に並べ替え
    sortedList = sorted(list(fizzbuzzDict.keys()))
    #出力用文字列
    outputList = ''

    #文字列作成
    for checkNumber in sortedList:
        if number % checkNumber == 0:
            outputList += fizzbuzzDict[checkNumber]

    #表示
    if outputList:
        print(outputList)
    else:
        print(number)





if __name__ == '__main__':
    main()
