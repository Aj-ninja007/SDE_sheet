def negative(l):
    k = 3  # Window size
    i = 0  # Start of the window
    j = 0  # End of the window
    n = len(l)
    ans = []
    que = []
    
    while j < n:
        # Add the current element to the queue if it is negative
        if l[j] < 0:
            que.append(l[j])
        
        # Check if we have reached the window size
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            # If the queue is not empty, the first element is the first negative in the window
            if que:
                ans.append(que[0])
            else:
                ans.append(0)  # No negative number in this window
            
            # Slide the window forward
            print(que)
            if que and l[i] == que[0]:
                que.pop(0) 
            
            i += 1
            j += 1
    
    return ans

l = [12, -1, -7, 8, -15, 30, 16, 28]
print(negative(l))
