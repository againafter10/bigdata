import random,string
import os

chars=string.ascii_uppercase + string.digits

base_dir="/home/cloudera/apachesprak/spooldata"
ext=".txt"
str=""
os.chdir(base_dir)
#while True:
for i in range(10):
    str=''.join(random.choice(chars) for _ in range(10))
    str=str + ext
    print(str)
    with open(str, "w") as f:
       f.write("I am an example.")
    str=""
    print


