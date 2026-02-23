class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def analize_list(head):
    current = head
    i = 0
    sum = 0
    while current:
        i = i + 1
        sum = sum + current.value
        current = current.next
    
    print("Number of elements", i)
    print("sum of elements", sum)

def convert_list(head):
    dummy = ListNode(0)
    current = dummy
    for num in head:
        current.next = ListNode(num) # Create new node
        current = current.next
    return dummy.next

listNum = [1, 2, 3, 4, 5]
convertedList = convert_list(listNum)
print(analize_list(convertedList))





def lengthOfLongestSubstring(s):
        substr = ""
        i = 0
        count = 0
        if len(s) < 3: return
        for char in s:
            if substr.find(char):
                substr.__add__(char)
                i = i + 1
                if len(substr) == 3: 
                    count = count + 1
                    s.removeprefix(substr)
                    lengthOfLongestSubstring(s) 
            i = i + 1
        return

string = "abcabcbb"
print(lengthOfLongestSubstring(string))


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(elements):
    if not elements:
        return None
    
    head = Node(elements[0])
    current = head
    
    for value in elements[1:]:
        current.next = Node(value)
        current = current.next
        
    return head

def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))

def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next  
        current.next = prev       
        prev = current            
        current = next_node      
    return prev

def find_middle(head):
    current = head
    dcurrent = head
    while dcurrent != None and dcurrent.next != None:
        dcurrent = dcurrent.next.next
        current = current.next
    return current

my_data = [10, 20, 30, 40, 50]
linked_list_head = create_linked_list(my_data)
middleNode = find_middle(linked_list_head)
print(middleNode.val)
print("Original Linked List:")
print_linked_list(linked_list_head)

reversed_head = reverse(linked_list_head)

print("\nReversed Linked List:")
print_linked_list(reversed_head)
        
stack = ["(", ")", ")", ")"]
def isBalanced(stack):
    for i in stack:
        last = stack.pop()
        if i == last:
            return False
    return True

def is_balanced(s):
    waiting_room = []
    
    for char in s:
        if char == "(":
            waiting_room.append(char)
        elif char == ")":
            # Check if waiting room is empty
            if not waiting_room:
                return False
            # Found a pair! Remove the opener.
            waiting_room.pop()
            
    # If room is empty at the end, everyone found a partner. True.
    return len(waiting_room) == 0

# Test
print(is_balanced("(())"))  # True
print(is_balanced("(()"))   # False (one '(' left in room)
print(is_balanced("())"))   # False (found ')' but room was empty)

print(is_balanced(stack))
