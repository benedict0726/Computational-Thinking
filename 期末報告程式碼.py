#chat robot
#延遲函數
def right():
    import time
    time.sleep(1)
def wrong():
    import time
    time.sleep(1.5)
def answer():
    import time
    time.sleep(1.25)
print("嗨!我叫Mrs.吉蛙蛙，可以叫我小吉，很高興認識你。")
hobby="我很喜歡吃東西，同時也喜歡養寵物，今天遇到你一定是一種緣份，很高興認識你。"
print(hobby)
#基本問題
name=input("那麼你的名字是?:")
right()
print("你叫", name, "對吧，真是一個好名字，很高興認識你!")
#基本對話與結尾
w=1
while(w!=0):
    q=int(input("\n你想跟我聊什麼?(1)食物、(2)動物、(3)心理測驗、(4)天氣、(5)數學測驗、(6)運動、(7)音樂，輸入(0)結束聊天:"))
    if(q==0):
        print("今天很高興與你對話，", name, "，我很期待我與你下次的對話。")
        import time
        time.sleep(2)
        for a in range (3,0,-1):
            print(a)
        print("shut down")
        break
    elif(q==1):
        print("我很喜歡吃甜食，巧克力、蛋糕等等，只要是甜的我都可以接受")
        food_list=["巧克力", "抹茶", '蛋糕餅乾', '派', '甜甜圈']
        print(food_list)
        input('你覺得我最喜歡吃哪個?:')
        answer()
        x=int(input('我最喜歡吃抹茶了，你猜對還是猜錯呢?(1)猜對(2)猜錯'))
        if(x==1):
            answer()
            print('你真厲害，加你一分')
        else:
            answer()
            print('真是可惜，扣一分')
        print('但是除了抹茶外，我也推薦這些')
        main_dessert=['巧克力', '布丁', '蛋糕', '車輪餅', 'OREO']
        minor_dessert=['配香蕉', '配焦糖', '配咖啡', '選奶油口味', '配牛奶']
        for a in range(0,5,1):
            print(main_dessert[a], minor_dessert[a],end=' ')
    elif(q==2):
        pet=int(input("說到寵物，我最喜歡貓了，無聊的時候跟貓玩是一個非常簡單殺時間的方法，那麼你貓派還是狗派?(1)貓派、(2)狗派"))
        if(pet==1):
            answer()
            print("原來你跟我一樣喜歡貓啊，看來我們能成為不錯的朋友呢。")
            cat=['波斯貓', '英國短毛貓', '虎斑貓', '摺耳貓', '橘貓']
            print(cat)
            v=input('你喜歡哪一種還是其他的?:')
            print('你喜歡', v, '，我可以考慮養看看')
            types=['可愛', '偏醜', '眼睛大大的', '很呆的']
            print('反正不管是',end=' ')
            for g in range (0,4,1):
                print(types[g],end=' ')
            print('，只要是貓我都喜歡')
        else:
            answer()
            print("我也很喜歡狗，看來我們能成為很好的朋友呢。")
            dog=['黃金獵犬', '博美', '哈士奇', '台灣土狗', '吉娃娃']
            print(dog)
            v=input('你喜歡哪一種還是其他的?:')
            print('你喜歡', v, '，我可以考慮養看看')
            types=['可愛', '偏醜', '眼睛大大的', '很呆的']
            print('反正不管是',end=' ')
            for g in range (0,4,1):
                print(types[g],end=' ')
            print('，只要是狗我都喜歡')
    elif(q==3):
        r=int(input('最近我在網路上看到一個心理測驗我覺得很準，我想給你試試看可以嗎?(1)可以(2)不可以'))
        if(r==1):
            answer()
            print('哇，謝謝來玩玩看吧')
        else:
            answer()
            print('你沒有選擇的餘地，你還是要玩')
        chose=['A', 'B', 'C', 'D']
        answer=['美景如此動人，不理會這些人', '對被打擾很生氣，決定結束旅程', '海邊還有很多地方，遠離他們繼續欣賞', '繼續欣賞，但是心理很不爽，咒罵他們趕緊走']
        heart=['情緒壓抑，日常生活都你都會盡量保持完美，不敢表達自己，心裡可能比較壓抑', '以往的內心困然，對於自己曾經犯下的錯牢記於心，就算努力改正也一樣自責，不敢給別人發現，不然會很難受', '生活習慣不一致，比較注重於外表，但私下可能比較邋遢，只是希望有比較多朋友，但是很有少朋友能介入你的私生活', '內心感情混亂，你愛好交際，但可能帶給自己太多感情困擾，所以你把表面跟私下分的很清楚，且保持與私生活相反的生活，因為你知道這一切會帶給妳很多損失']
        print('正值假期，你獨自坐在海邊欣賞美景。就當你沉醉在美景之時，幾個語言粗魯、樣貌不討喜的人打亂了這美好的平靜，你會怎樣做呢？')
        for t in range(0,4,1):
            print(chose[t], answer[t])
        print('給你7秒時間想')
        import time
        time.sleep(7)
        for u in range(0,4,1):
            print('選', chose[u], '，',heart[u] )
        print('是不是很準阿')
    elif(q==4):
        print("今天天氣如何呢?")
        a=int(input('(1)有降雨(2)無降雨'))
        if(a==1):
            probability=['毛毛雨', '陣雨', '大雨', '豪大雨']
            print(probability)
            z=input('是哪一個呢?:')
            answer()
            print('原來是', z, '要記得帶傘歐')
        else:
            probability=['晴天', '多雲', '陰天']
            print(probability)
            z=input('是哪個呢')
            answer()
            print('原來是', z, '在文山區很少能見到這種天氣呢')
        main=['上午晴天', '上午下雨', '整天', '整天', '整天']
        minor=['下午下雨', '下午放晴', '下雨', '放晴', '陰天']
        print('每次都是',end=' ')
        for w in range(0,5,1):
            print(main[w], minor[w], '，',end=' ')
        print('有太陽就不錯了')
    elif(q==5):
        test=int(input("那既然前面已經稍微測試過你的數學能力了，那就讓我們來做更進階的數學測試吧！(1)yes(2)no"))
        if(test==1):
            answer()
            print("那我們來做九九乘法表的測試吧！先讓你看一下九九乘法表複習一下！～")
            for i in range(1,10):
                for j in range(1,10):
                    print('{0:2d}*1={2:2d}'.format(i,j,i*j), end=' ')
                print()
        elif(test==2):
            answer()
            print("抱歉，沒有你選擇的餘地")
        else:
            answer()
            print("輸入錯誤，請重新輸入，只能選yes/no ")
        question=int(input("那現在到我測試你的時間了！請問9*9是多少呢？"))
        if(question==81):
            answer()
            print("太棒了，你答對了！接著看下面一題～")
        else:
            wrong()
            print("沒關係，下一題再接再厲！")
        question_two=int(input("第二題，請問8*7是多少呢？"))
        if(question_two==56):
            right()
            print("你好厲害，你答對了")
        else:
            wrong()
            print("不要氣餒，未來的日子你一定可以翻盤！")
        math=int(input("剛剛的問題你對了幾題呢？（1)0題 （2)1題 (3)2題"))
        if(math==1):
            answer()
            print("啊糟糕！但沒關係經過我之後耐心的教導，相信你的數學絕對能夠變成第一名！")
        elif(math==2):
            answer()
            print("不錯哦！但還有進步空間，再接再厲！")
        elif(math==3):
            answer()
            print("很棒耶！看來沒有需要我教導的地方了～：)")
        else:
            print("請在a~c的選項中做選擇！")            
    elif(q==6):
            print("我很熱愛打籃球，跑步、羽毛球等等，只要是運動我都喜歡")
            interest_list=["籃球", "羽毛球", "跑步", "排球", "有氧"]
            print(interest_list)
            input("你覺得我最喜歡哪個運動?")
            answer()
            x=int(input("我最喜歡打籃球，你猜對還是猜錯?(1)猜對(2)猜錯"))
            if(x==1):
                print("你真厲害，加你一分")
            else:
                print("真是可惜，扣一分")
            sport=["羽毛球", "跑步", "排球", "有氧", '撞球', '等等球類運動']
            print("雖然籃球是我的最愛，但是其他運動我也很喜歡，像是", end=' ')
            for s in range (0,6,1):
                print(sport[s], end=' ')
            print("這些我也很喜歡")
    elif(q==7):
        print("我喜歡聽古典樂，流行樂，爵士樂等等，只要是音樂我都喜歡")
        music_list=["古典樂", "流行樂", "爵士樂", "嘻哈", "搖滾"]
        print(music_list)
        input("你覺得我最喜歡哪種音樂?")
        answer()
        x=int(input("我最喜歡流行樂，你猜對還是猜錯?(1)猜對(2)猜錯"))
        if(x==1):
            print("你真厲害，加你一分")
        else:
            print("真是可惜，扣一分")
        music=["古典樂", "流行樂", "爵士樂", "嘻哈", "搖滾", "等等音樂種類"]
        print("\n雖然流行樂是我的最愛，但是其他音樂種類我也很喜歡，像是", end=' ')
        for s in range (0,6,1):
            print(music[s], end=' ')
        print("這些我也很喜歡")
    else:
        print("跟你說了只有0~4而已。")
