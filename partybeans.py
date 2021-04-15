def main():
    total = 0
    total_check = False
    while not total_check:
        try:
            total = int(input("輸入本周累積消費K豆："))
            print("---------------")
            total_check = True
        except ValueError:
            print("輸入數字啦吼")

    if total < 100000:
        reward = 0
    elif total < 500000:
        reward = 15000
    elif total < 1000000:
        reward = 75000
    elif total < 3000000:
        reward = 150000
    elif total < 5000000:
        reward = 450000
    elif total < 10000000:
        reward = 750000
    else:
        reward = 1500000
    print("可分配反豆總數：{}\n---------------".format(reward))

    people = []
    total = 0
    num_people = 0
    num_people_check = False
    while not num_people_check:
        try:
            num_people = int(input("輸入要反豆人數："))
            print("---------------")
            num_people_check = True
        except ValueError:
            print("錯誤！輸入數字喔\n---------------")

    for i in range(num_people):
        person_check = False
        while not person_check:
            try:
                person = int(input("輸入第{}位刷豆數量：".format(i + 1)))
                people.append(person)
                total += person
                person_check = True
            except ValueError:
                print("我說 輸 入 數 字")

    person_reward_list = []
    reward_total = 0
    for i, person in enumerate(people):
        person_reward = (person * reward) // total
        person_reward_list.append(person_reward)
        reward_total += person_reward

    beanleft = reward - reward_total
    while beanleft != 0:
        for i in range(beanleft):
            person_reward_list[i] += 1
            beanleft -= 1

    print("---------------\n計算結果：\n")
    for i, person_reward in enumerate(person_reward_list):
        print("第{}位反豆數：{}".format(i + 1, person_reward))


if __name__ == '__main__':
    main()
