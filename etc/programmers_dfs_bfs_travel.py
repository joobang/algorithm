from collections import deque

def solution(tickets):
    answer = []
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
       
    
    
    for i in range(len(tickets)):
  
        if i == 0:
            answer.append("ICN")
            curr_end = ticket_dict["ICN"].pop()
            answer.append(curr_end)
        else:
            if len(ticket_dict[curr_end]) > 0:
                curr_end = ticket_dict[curr_end].pop()
                answer.append(curr_end)
    
    
            
    
    return answer