import random
from tqdm import tqdm
from urllib.request import urlopen
print("请输入你要添加的内容a：")
a= input("请输入：")
print("请输入你要添加的内容b: ")
b =input("请输入：")
cishu = input("请输入你想执行的次数:")
for i in tqdm(range(int(cishu))):
    u = random.randint(10000000, 999999999)
    p = random.randint(1000000000, 99999999999)
    url = f"http://xyw.xxwtd.store/status.php?action=add&u={i}{u}&p={a}{p}&id=&system_str=PC"
    url2 = f"http://xyw.xxwtd.store/status.php?action=add&u={i}{u + 1}&p={b}{p - 1}&id=&system_str=Android"
    p = urlopen(url).read().decode("utf-8")
    p2 = urlopen(url2).read().decode("utf-8")
    #print(f"{p}\n{p2}")
print(f"{cishu}次执行完毕")