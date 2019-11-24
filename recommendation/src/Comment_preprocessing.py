# -*- coding:utf-8 -*-
from konlpy.tag import Okt
from collections import Counter
from TF_IDF import *
import os

twitter = Okt()
stopword = []
# stopword 파일을 읽어 stopword list에 저장
f = open('../stopwords-ko.txt', 'rt', encoding='UTF8')

while True:
    line = f.readline().rstrip('\n')
    if not line:
        break
    stopword.append(line)
f.close()

#print(stopword)

# 댓글의 형태소 분석
def PreprocessComment(Comment):
    Comment_word = []
    tokens = twitter.Okt.pos(Comment, norm=True, stem=False)
    # Noun 만 골라서 담기
    for i in tokens:
        if i[1] == "Noun":
            #stopword 에 없는지도 확인
            if i[0] not in stopword:
                Comment_word.append(i[0])
    return Counter(Comment_word)


# DataSet 의 전처리 과정 (만약에 txt로 저장해서 할거면 이거 사용)
def PreprocessFiles(file_dir):
    All_tagged_list = []
    path_list = [os.path.join(file_dir, file_name) for file_name in os.listdir(file_dir)]
    for i in path_list:
        temp = []
        with open(i, 'rt', encoding='UTF8') as file:
            print(file)
            for line in file:
                line = line.replace("\n", "")
                tagged_list = twitter.pos(line, norm=True, stem=False)
                for j in tagged_list:
                    # stopwords 거나 noun 이 아니라면 제외!
                    if j[1] == "Noun" and j[0] not in stopword and len(j[0]) != 1:
                        if j[0] == "별표" or j[0] == "개":
                            # 평점 기입부분은 파싱해서 제외처리
                            pass
                        else:
                            #print(j[0])
                            temp.append(j[0])
        All_tagged_list.append(Counter(temp))
    return All_tagged_list

predata = PreprocessFiles('../text_data')
for i in predata:
    print(i)

# test main code

# with open('../text_data/남산.txt', 'rt', encoding='UTF8') as file:
#     temp = []
#     All_tagged_list = []
#     for line in file:
#         line = line.replace("\n", "")
#         tagged_list = twitter.pos(line, norm=True, stem=False)
#         for j in tagged_list:
#             # stopwords 거나 noun 이 아닌경우 제외
#             if j[1] == "Noun" and j[0] not in stopword and len(j[0]) != 1:
#                 temp.append(j[0])
# All_tagged_list.append(Counter(temp))
# print(All_tagged_list)
# print(Indexing(All_tagged_list))
# test = Counter(temp)
# print(test.most_common(20))
#
# for i in test:
#     if test[i] > 50:
#         print("yes!")
