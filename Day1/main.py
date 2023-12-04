
reader = open('day1.txt', 'r')
Lines = reader.readlines()
count = 0
lineCount = 0
currCount = 0
listCounter = []
finalCount = []
wordValue = ''

for x in Lines:
    #print(x.strip())
    intCheck = x.strip()
    print('Curr Line: ',intCheck)
    for y, c in enumerate(intCheck):
        print(c)
        if intCheck[y].isdigit():
            print('is digit!')
            #addition check it works
            #lineCount = int(intCheck[y]) + lineCount
            listCounter.append(intCheck[y])

        else:
            wordValue = wordValue + c
            print('building value: ',wordValue)
            if wordValue == 'one' or wordValue == 'two' or wordValue == 'three' or wordValue == 'four' or wordValue == 'five' or wordValue == 'six' or wordValue == 'seven' or wordValue == 'eight' or wordValue == 'nine':
                print('BUILT VALUE!: ', wordValue)
                if wordValue == 'one':
                    print('1')
                    listCounter.append('1')
                elif wordValue == 'two':
                    print('2')
                    listCounter.append('2')
                elif wordValue == 'three':
                    print('3')
                    listCounter.append('3')
                elif wordValue == 'four':
                    print('4')
                    listCounter.append('4')
                elif wordValue == 'five':
                    print('5')
                    listCounter.append('5')
                elif wordValue == 'six':
                    print('6')
                    listCounter.append('6')
                elif wordValue == 'seven':
                    print('----------ADDING 7 TO LIST COUNTER-----------')
                    listCounter.append('7')
                elif wordValue == 'eight':
                    print('8')
                    listCounter.append('8')
                elif wordValue == 'nine':
                    print('9')
                    listCounter.append('9')
        

            else:
                print("not building")
        

    

    #reset the list for the next in check
    currCount = listCounter[0] + listCounter[-1]
    finalCount.append(int(currCount))
    print(listCounter)
    #for safety idk what i'm doing
    currCount = 0
    listCounter = []
    wordValue = ''
    #for z in lineCount:
        
    



total = sum(finalCount)
print(count)
print(finalCount)
print(total)