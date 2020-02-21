def toListNode(arr):
    root = ListNode(None)
    nextNode = root
    for el in arr:
        nextNode.val = el
        nextNode.next = ListNode(None)
        nextNode = nextNode.next
    return root


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        result_representation = ""
        while self is not None:
            result_representation = result_representation + str(self.val)
            if self.next is not None:
                result_representation = result_representation + " -> "
            self = self.next
        return result_representation


class Solution(object):
    def addTwoNumbers(l1, l2):
        sum_result_root = ListNode(None)
        sum_result = sum_result_root
        sum_remains = 0
        while l1.val is not None or l2.val is not None:
            digits_sum = (l1.val or 0) + (l2.val or 0) + sum_remains
            if digits_sum <= 9:
                sum_result.val = digits_sum
                sum_remains = 0
            else:
                sum_result.val = (digits_sum % 10)
                sum_remains = 1
            sum_result.next = ListNode(None)
            prev_sum_result = sum_result
            sum_result = sum_result.next
            l1 = l1.next or ListNode(None)
            l2 = l2.next or ListNode(None)

        if sum_remains:
            sum_result.val = sum_remains
        else:
            prev_sum_result.next = None
        return sum_result_root


print(Solution.addTwoNumbers(toListNode([2, 4, 3]), toListNode([5, 6, 4])))
print(Solution.addTwoNumbers(toListNode([9, 9, 9, 9]), toListNode([9, 9, 9, 9, 9, 9, 9, 9])))
print(Solution.addTwoNumbers(toListNode([9, 9, 9, 9]), toListNode([0])))
print(Solution.addTwoNumbers(toListNode([0]), toListNode([0])))
print(Solution.addTwoNumbers(toListNode([0]), toListNode([1])))
print(Solution.addTwoNumbers(toListNode([0]), toListNode([0, 1])))
print(Solution.addTwoNumbers(toListNode([0, 1]), toListNode([0, 1])))
print(Solution.addTwoNumbers(toListNode([1, 7, 8, 7, 5]), toListNode([3, 2, 0, 6])))  # 63894

# Test case
# [2,4,3]
# [5,6,4]
# [9,9,9,9]
# [9,9,9,9,9,9,9,9]
# [1,7,8,7,5]
# [3,2,0,6]
# [0]
# [0]
# [0]
# [1]
# [0]
# [0,1]
# [0,1]
# [0,1]
# [3,4,6,1,0,7,6,5,1]
# [8,5,1,9,7,1,6,6,9]