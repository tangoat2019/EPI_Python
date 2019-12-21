class MergeTwoSortedList:
    def merge(self, L1, L2):
        while L1 and L2:
            if L1 or L2:
                temp.next = L1 or L2
            if L1.data < L2.data:
                temp, L1.next = L1.next, array2
                merge(temp,L2)
            else:
                temp, L2.next = L2.next, L1
                merge(temp, L1)