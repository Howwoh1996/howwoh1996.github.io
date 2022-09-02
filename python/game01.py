# 遊戲規則:吹氣球 每吹一次有不同的機率會爆炸 把氣球綁起來 會獲得關於氣球大小的積分 並再吹下一顆
# 爆炸獲得 30%分數 
# 吹氣球 破掉機率 0 , 0.02 , 0.04 , 0.07 , 0.1 ,0.15 , 0.2 , 0.25 , 0.3 , 0.4 , 0.5
# 積分增加 2000 2800 3600 4400 5200 6000 6800 7600 8400 9200
# 積分累加 2000 4800 8400 12800 18000 24000 30800 38200 46800 
# 找出最好的策略 可以獲得最多的分數
import random
blow_posibilitly=[0 , 0.02 , 0.04 , 0.07 , 0.1 ,0.15 , 0.2 , 0.25 , 0.3 , 0.4 , 0.5 ,0.6,0.7,0.8,0.9,0.95,1]
blow_point=[2000+800*x for x in range(16)]
blow_total_point=[sum(blow_point[:x+1]) for x in range(15)]
times_arr=[x+1 for x in range(9)]
def point_count(times_in_function):
    #足夠大的數字 可以使誤差將低
    total_times=1000000 
    #初始化目前氣球大小為0 (0次吹氣)
    blow_times=0 
    #初始化得分為0
    point=0 
    for _ in range(total_times):
        blow_times+=1
        # 判定有沒有吹破
        if(random.random()<blow_posibilitly[blow_times-1]):
            #吹破獲得分數為當前分數*0.3
            point+=blow_total_point[blow_times-2]*0.3
            #氣球大小歸0
            blow_times=0
        #若達到指定大小 則綁起氣球
        elif(blow_times>=times_in_function):
            #得分為吹完後的大小之分數
            point+=blow_total_point[blow_times-1]
            #氣球大小歸0
            blow_times=0
    return point/total_times #平均得分
rank=[(x,point_count(x)) for x in times_arr]
#排序後 將資料印出來
print(sorted(rank, key=lambda r:r[1],reverse=True))


