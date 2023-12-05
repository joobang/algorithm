from collections import deque

def solution(tickets):
    answer = []
    path = []
    ticket_dict = {}
    curr_end = ""
    
    for i in range(len(tickets)):
        start = tickets[i][0]
        end = tickets[i][1]
        
        if start in ticket_dict:
            ticket_dict[start].append(end)
            ticket_dict[start].sort(reverse=True) 
        else:
            ticket_dict[start] = [end]
       
    
    print(ticket_dict)
    #print(ticket_dict.get("ICN"))
    def dfs(airport):
        print("airport : ", airport)
        while ticket_dict.get(airport):
            dfs(ticket_dict[airport].pop())
        answer.append(airport)
        print(answer)

    dfs("ICN")
        
    return answer[::-1]

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "A"], ["ICN", "B"], ["B", "ATL"], ["ATL", "ICN"]])