#project_title專題題目
#name_list成員姓名
name=['林郁婷', '陳妤瑄', '林嘉欣', '甘庭銨', '游佳樺', '蔡柏薪', '林昱承', '簡郁虹', '王子維']
#number_list成員學號
number=['A109260010','A109260028', 'A109260036', 'A109260038','A109260042', 'A109260044', 'A109260046', 'A109260074', 'A109260096' ]
#duty_list分工內容
duty=['聊天內容', '程式碼']
#load_list分工比重
load=['5%','10%','15%']
#code程式碼
print('專題題目:聊天機器人')
print('組長:', name[3])
print('成員名單:')
for a  in range (0,9,1):
    print(a+1,'.', name[a], number[a], '、', end=' ')
print(duty[0], ':', name[0], name[1], name[2], name[4])
print(duty[1], ':', name[3], name[5], name[6], name[7], name[8])
print('分工比重:')
print(load[2], ':', name[3], name[5])
print(load[1], ':', name[0], name[1], name[2], name[4], name[6], name[7], name[8])