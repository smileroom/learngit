import random


accuracy =0
count = 0


def number():
    i = random.randint(1,100)
    return i

def mathSymbol():
    symbol = ['+','-',  '*' ,'÷' ]
    d = random.choice(symbol)
    return d
def main():
    global accuracy 
    symbolOne = mathSymbol()
    one = number()
    two = number()
    if one > two:
        numberOne = one
        numberTwo = two
    else:
        numberOne = two
        numberTwo = one
    print("请计算:  %d %s %d = " % (numberOne, symbolOne, numberTwo))
    if symbolOne == '+':
        result = numberOne + numberTwo
    elif symbolOne == '-':
        result = numberOne - numberTwo
    elif symbolOne == '*':
        result = numberOne * numberTwo
    elif symbolOne == '÷':
        result = numberOne // numberTwo
        other = numberOne - (result * numberTwo)
    print(result)
    if symbolOne == '÷':
        anwser = input("请输入您的答案(除法)：")
        anwser = anwser.strip()
        anwserTwo = input("请输入余数：")
        anwserTwo = anwserTwo.strip()
        if not anwser.isdigit() or not anwserTwo.isdigit() :
            print("非法输入，请输入数字")
        elif anwser == str(result) and anwserTwo == str(other):
            print('计算正确')
            accuracy=accuracy+1
        else:
            print('计算错误')
    else:
        anwser = input("请输入您的答案：")
        anwser = anwser.strip()
        if not anwser.isdigit():
            print("非法输入，请输入数字")
        elif anwser == str(result):
            print('计算正确')
            accuracy=accuracy+1
        else:
            print('计算错误')
sum =input("请输入测试练习题数目：")
sum = int(sum.strip())
print('开始%d道题的测试练习'%sum)
print('输入 e 离开题目练习')
while count < sum:
    count+=1
    print("第"+str(count)+"道数学题")
    main()
    if count == sum:
        accuracy = (accuracy / sum) * 100
        print('%d道题准确率为%.2f%% ' %(sum,accuracy))
    exit = input()
    if exit =='e':
        print('选择离开题目练习')
        break
    else :
        continue



