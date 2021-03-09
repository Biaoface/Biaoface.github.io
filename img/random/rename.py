
cout = 0
import os
import re
for file in os.walk("."):
    t = list (file)
l = t[2]
l.remove("rename.py")
for i in l:
    r = re.search("material-", i)
    if r == None:
        cout = cout + 1
        des = "material-" + str(cout) + ".png"
        os.rename(i, des)
print ("一次性改名脚本执行成功")

        
        
            




