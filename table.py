import os
cn=["DiSanXian","DuoJiaoYuTou","GanBianSiJiDou","HongShaoDaiYu","HongShaoPaiGu","HongShaoRou","HongShaoShiZiTou","HongShaoZhuTi","JiDanBing","JiangNiuRou","LaZiJi","MaPoDouFu","MeiCaiKouRou","PaoJiaoFengZhao","SuanLaTuDouSi","XiHongShiChaoJiDan","XiangLaXia","YuXiangQieZi","ZhaJiangMian","ZhenZhuWanZi"]
ds=["Sauteed Potato, Green Pepper and Eggplant","Steamed Fish Head with Diced Hot Red Peppers","Dry-Fried Green Beans with Minced Pork and Preserved Vegetables","Braised Hairtail in Brown Sauce","Spareribs with brown sauce","Pork braised in brown sauce","Stewed Pork Ball in Brown Sauce","Braised Pork Trotter with Soya Sauce","Egg cake","Beef in Brown Sauce","Spicy chicken","Mapo Tofu","Braised Pork with Preserved Vegetable in Soya Sauce","Chicken Feet with Pickled Peppers","Sour and spicy shredded potatoes","Scrambled egg with tomato","Fried Shrimps in Hot and Spicy Sauce","Yu-Shiang Eggplant","Noodles with Soy Bean Paste","Meat ball"]
nn=["4333","3041","3499","3494","3457","4271","4036","4201","4063","3648","3317","3001","4181","3167","3346","3581","3468","3492","4502","3027"]

f=open('temp.txt','w')
print len(cn),len(ds),len(nn)
ct=0
for i in cn:
    print ct,i
    ct+=1
for i in range(20):
    xr="\hline "+'&'.join([cn[i],ds[i],nn[i]])+"\\" + "\\"+'\n'
    f.write(xr)
f.close()