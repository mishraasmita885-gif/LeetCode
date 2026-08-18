Approach:

I used the Slow and Fast Pointer approach.

I created two pointers: slow and fast.
Both pointers start from the head of the linked list.
slow moves one node at a time.
fast moves two nodes at a time.
When fast reaches the end of the linked list, slow will be at the middle node.
For an even number of nodes, this approach automatically gives the second middle node, as required by the problem.

Example:

For:

1 → 2 → 3 → 4 → 5

The pointers move like:

slow: 1 → 2 → 3
fast: 1 → 3 → 5

When fast reaches the end, slow is at 3, which is the middle.

For:

1 → 2 → 3 → 4 → 5 → 6

slow reaches 4, which is the second middle node.

Code Logic :

slow = head
fast = head

while fast and fast.next:
    slow moves one step
    fast moves two steps

return slow

Complexity
Time Complexity: O(n)
Space Complexity: O(1)
Key Learning

The important idea I learned from this problem is that two pointers moving at different 
speeds can be used to find the middle of a linked list without calculating its length first.
