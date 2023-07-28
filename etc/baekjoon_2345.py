
# def solution(happy,angry,sad,joy,song):
#     answer = []
    
    
#     for s in song:
#         song_words = s.split()
#         answer_dic = {'happy':0,'angry':0,'sad':0, 'joy':0}
#         song_dic = {}
#         for word in song_words:
#             if song_dic.get(word) is None:
#                 song_dic[word] = 1
#             else:
#                 song_dic[word] += 1
        
#         for key in song_dic.keys():
#             if key in happy:
#                 answer_dic['happy'] += song_dic[key]
#             elif key in angry:
#                 answer_dic['angry'] += song_dic[key]
#             elif key in sad:
#                 answer_dic['sad'] += song_dic[key]
#             elif key in joy:
#                 answer_dic['joy'] += song_dic[key]
                
#         #print(song_dic)
#         #print(answer_dic)
#         #print(max(answer_dic, key=answer_dic.get))
#         answer.append(max(answer_dic, key=answer_dic.get))
        
#     return answer

# print(solution(
#     ['good','thrilled'],
#     ['annoyed'],
#     ['mournful','melancholy'],
#     ['gladness'],
#     ['mournful gladness mournful','annoyed gladness good thrilled','mournful melancholy melancholy']
# )
# )
from typing import List

def make_words(k:int, word:str):
    answer = []
    dot_index = word.find('.')
    word_list = list(word)
    word_list[dot_index] = ''
    
    for i in range(dot_index, dot_index+k):
        #print(word_list[i])
        word_list.insert(i,'*')
        answer.append(''.join(word_list))
    for a in answer:
        if '.' in a:
            answer += make_words(k,a)
    
    return answer

def solution(k: int, dic: List[str], chat:str):
    answer = ''
    answer_list =[]
    chat_list = chat.split()
    
    for i in range(len(chat_list)):
        if chat_list[i] in dic:
            re_chat = '#' * len(chat_list[i])
            answer_list.append(re_chat)
        elif '.' in chat_list[i]:
            #print(chat_list[i])
            dot_list = make_words(k,chat_list[i])
            #print(dot_list)
            
            isMatch = False
            isBreak = False
            # 점이 있는 모든 경우의 수를 사전과 비교
            for dot_word in dot_list:
                for dic_word in dic:
                    #print('dic_word : ',dic_word)
                    # 길이 같은 경우만 치환문자들이 같은지 비교
                    if len(dic_word) == len(dot_word):
                        # 비교할 점이 있던 문자열의 만능 알파벳 인덱스 구하기
                        dot_word_list = list(dot_word)
                        dic_word_list = list(dic_word)
                        for j in range(len(dot_word_list)):
                            if dot_word_list[j] == '*':
                                dic_word_list[j] = '*'
                        
                        dic_word = ''.join(dic_word_list)
                        
                        #print('dicword : ',dic_word)
                        # 채팅로그 치환문자와 사전단어(치환된)와 같은 경우
                        if dic_word == dot_word:
                            #print('match : ',dic_word)
                            isMatch = True
                            isBreak = True
                            break
                    # 길이가 다른경우 다른 경우의수로 넘어감    
                    else:
                        #print('diff len : ',dic_word, dot_word)
                        pass
                
                # 길이가 다른 경우 반복문을 끝낸다
                if isBreak:
                    break
            
            if isMatch:
                re_chat = '#' * len(chat_list[i])
                answer_list.append(re_chat)
            else:
                answer_list.append(chat_list[i])
            
        else:
            answer_list.append(chat_list[i])
    
    #print(answer_list)
    answer = ' '.join(answer_list)
    return answer

print(solution(2,['slang','badword'],'badword ab.cd bad.ord .word sl.. bad.word'))
#print(solution(3,['abcde','cdefg','efgij'],'.. ab. cdefgh .gi. .z.'))