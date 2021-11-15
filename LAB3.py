# LAB3
# Due Date: 10/01/2021, 11:59PM
# REMINDERS: 
#        The work in this assignment must be your own original work and must be completed alone.
#        All functions should NOT contain any for/while loops or global variables. Use recursion, otherwise no credit will be given

def get_count(aList, item):
    '''
        >>> get_count([1,4,3.5,'1',3.5, 9, 1, 4, 2], 1)
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 3.5)  
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 9)   
        1
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 'a') 
        0
    '''
    if aList[0] == item: # base case that checks if the first index of the list is equal to the item
        return 1 + get_count(aList[1:], item) # adds the count then decriments list and uses recursion to call it again
    else:
        if item not in aList:
            return 0
        return 0 + get_count(aList[1:], item) #decriments list and uses recursion to call it again








def replace(numList, old, new):
    '''
        >>> input_list = [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace(input_list, 1, 99.9)
        [99.9, 7, 5.6, 3, 2, 4, 99.9, 9]
        >>> input_list
        [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 5.6, 777) 
        [1, 7, 777, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 8, 99)    
        [1, 7, 5.6, 3, 2, 4, 1, 9]
    '''

    if len(numList) == 1:
        if numList[0] == old:
            return [new] #returns the number in a new list
        else:
            return numList #returns original 
    else:        
        if numList[0] == old:
            return [new] + replace(numList[1:], old, new) #returns new, uses recursion to add it and calls function again while decrimenting the list shorter
        else:
            return [numList[0]] + replace(numList[1:], old, new) 





def flat(aList):
    '''
        >>> x = [3, [[5, 2]], 6, [4]]
        >>> flat(x)
        [3, 5, 2, 6, 4]
        >>> x
        [3, [[5, 2]], 6, [4]]
        >>> flat([1, 2, 3])
        [1, 2, 3]
        >>> flat([1, [], 3])
        [1, 3]
    '''
    if len(aList) == 0:
        return aList #base case that states if no contents in alist, return it 
    if len(aList) > 0: #condition that states if there are contents in a list, continue
        if type(aList[0]) == list:
            return flat(aList[0]) + flat(aList[1:])  #descriments list down 
        elif type(aList[0]) == int:
            return [aList[0]] + flat([aList[1:]]) #decriments list down 




def neighbor(n):
    """
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
    """
    num_v = n//10 #new variable that operates floor division on n 
    if n == 0: #base case
        return n
    elif num_v % 10 == n%10: #first condition
        return neighbor(num_v) 
    else:
        return neighbor(num_v) * 10 + (n%10) #second condition

