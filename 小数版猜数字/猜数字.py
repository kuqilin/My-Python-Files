def getRandomNum():
    import random
    return random.uniform(0, 101)

def easy(goal):
    for i in range(100, 0, -1):
        puts = float(input('请输入1-100的数字：'))
        if puts == goal :
            print('恭喜你，猜对了！')
            exit()
        elif puts > goal :
            print(f'猜大了，你还有{i-1}次机会。{goal}')
        else :
            print(f'猜小了，你还有{i-1}次机会。')
    print('你输啦！')

def miduim(goal):
    for i in range(8, 0, -1):
        puts = float(input('请输入1-100的数字：'))
        if puts == goal :
            print('恭喜你，猜对了！')
            exit()
        elif puts > goal :
            print(f'猜大了，你还有{i-1}次机会。')
        else :
            print(f'猜小了，你还有{i-1}次机会。')

def difficult(goal):
    for i in range(5, 0, -1):
        puts = float(input('请输入1-100的数字：'))
        if puts == goal :
            print('恭喜你，猜对了！')
            exit()
        elif puts > goal :
            print(f'猜大了，你还有{i-1}次机会。')
        else :
            print(f'猜小了，你还有{i-1}次机会。')

def main():
    goal = getRandomNum()
    print('难度：\n1.简单（100次机会）\n2.中等（8次机会）\n3.困难（5次机会）\n请选择：')
    difficulty = int(input(''))
    if difficulty == 1 :
        easy(goal)
    elif difficulty == 2 :
        miduim(goal)
    elif difficulty == 3 :
        difficult(goal)
    else :
        print('')

if __name__ == '__main__' :
    main()