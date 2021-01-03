# https://hogni.tistory.com/45  중복 제거
# https://seyul.tistory.com/121 문자열 공백 제거 (치환)
# https://hwang-chive.tistory.com/10 파일 입출력

import re

filename = "data_raw.txt" # 처리할 파일 경로
myStr = []

f = open(filename)
lines = f.readlines()

cnt = 0

for line in lines:
  line = line.replace(" ,",",");
  line = line.replace(" .",".");
  line = line.replace("-", " / ");
  line = ' '.join(line.split()) # 2개이상 공백시 1개로 치환
  matchObj = re.search("(\d+)\.\s+",line)
  if matchObj != None:
    line = line.replace(matchObj.group(), "")
  line = line.strip()
  if line not in myStr:
    myStr.append(line)
    print(line)
    #       f.write(myStr)
    print(cnt)
    cnt += 1


  # print(myStr)
  # print(myStr.__len__())


f.close()
