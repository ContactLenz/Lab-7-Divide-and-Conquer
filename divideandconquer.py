import time

class ListNode:
    def __init__(self, value, link = None):
        self.value = value
        self.link = link

class LinkedList:
    def __init__(self, L=[]):
        self._head = None
        self._tail = None
        self._length = 0
        for i in L:
            self.addLast(i)

    def __iter__(self):
        self.current = self._head
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            temp = self.current.value
            self.current = self.current.link
            return temp

    def addFirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self._length += 1

    def addLast(self, item):
        if self._head is None:
            self.addFirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._length += 1

    def peekLast(self):
        if self._head:
            return self._tail.value
        return None

    def concatenate(self, other):
        if self._head:
            self._tail.link = other._head
            if other:
                self._tail = other._tail
        elif self._head is None:
            return other
        return self

    def __getitem__(self, i):
        cur = self._head
        for j in range(i):
            cur = cur.link
        return cur.value

    def __setitem__(self, i, item):
        cur = self._head
        for j in range(i):
            cur = cur.link
        cur.value = item

    def __str__(self):
        l = []
        cur = self._head
        while cur:
            l.append(cur.value)
            cur = cur.link
        return str(l)

    def __len__(self):
        return self._length

def splitTheList(L, mid):
    n = len(L)
    cur1 = L._head
    leftHalf = LinkedList()
    rightHalf = LinkedList()
    for i in range(mid):
        leftHalf.addLast(cur1.value)
        cur1 = cur1.link

    cur2 = L._head
    for i in range(mid):
        cur2 = cur2.link

    if cur2:
        for i in range(mid, n):
            rightHalf.addLast(cur2.value)
            cur2 = cur2.link
    return (leftHalf, rightHalf)

def mergeSort(L):
    # Base Case!
    if len(L) < 2:
        return L

    # Divide!
    mid = len(L) // 2
    leftHalf, rightHalf = splitTheList(L, mid)

    # Conquer!
    leftHalf = mergeSort(leftHalf)
    rightHalf = mergeSort(rightHalf)

    # Combine!
    return merge(leftHalf, rightHalf)


def merge(leftHalf, rightHalf):
  temp = LinkedList()
  A = leftHalf._head
  B = rightHalf._head

  while A and B:
      if A.value < B.value:
          temp.addLast(A.value)
          A = A.link
      else:
          temp.addLast(B.value)
          B = B.link

  if A is None:
      while B:
          temp.addLast(B.value)
          B = B.link
      temp._tail = rightHalf._tail
  elif B is None:
      while A:
          temp.addLast(A.value)
          A = A.link
  return temp

def identity(item):
    return item

def negative(item):
    return -1 * item

def unitsDigit(item):
    return item%10

# Part 1
def quickSortLinked(L):
    if len(L) < 2:
        return L
    pivot = L.peekLast()
    (list1, list2, list3) = splitLinkedList(L, pivot)
    listA = quickSortLinked(list1)
    listB = quickSortLinked(list2)
    listC = listA.concatenate(list3)
    return listC.concatenate(listB)

def splitLinkedList(L, pivot):
    list1 = LinkedList() #less than pivot
    list2 = LinkedList() #greater than pivot
    list3 = LinkedList() #equal to pivot
    for x in L:
        if x < pivot:
            list1.addLast(x)
        elif x > pivot:
            list2.addLast(x)
        else:
            list3.addLast(x)
    return (list1, list2, list3)

# Part 2
def quickSortInPlace(L, left = 0, right = None, keyFunc = identity):
    if right == None:
        right = len(L)
    if right - left > 1:
        mid = splitList(L, left, right, keyFunc)
        quickSortInPlace(L, left, mid, keyFunc)
        quickSortInPlace(L, mid+1, right, keyFunc)
    return L

def splitList(L, left, right, keyFunc):
    pivot = right - 1
    i = left
    j = pivot -1
    while i < j:
        while keyFunc(L[i]) < keyFunc(L[pivot]):
            i += 1
        while i < j and keyFunc(L[j]) >= keyFunc(L[pivot]):
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    if keyFunc(L[pivot]) <= keyFunc(L[i]):
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    return pivot

# Part 3 and 4
def quickSort(L, left=0, right=-1, keyFunc = identity):
    if right == None:
        right = len(L)
    if right - left > 1:
        pivot = right-1
        mid = partition(L, left, right, pivot, keyFunc)
        L1 = quickSort(L, left, mid, keyFunc)
        L2 = quickSort(L, mid+1, right, keyFunc)
    return L

def partition(L, left, right, pivot, keyFunc):
    i = left
    j = pivot - 1
    while i < j:
        while keyFunc(L[i]) < keyFunc(L[pivot]):
            i += 1
        while i < j and keyFunc(L[j]) >= keyFunc(L[pivot]):
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    if keyFunc(L[pivot]) <= keyFunc(L[i]):
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    return pivot

def rightMostDigit(item):
    return item % 10

## Part 5
def findKthLinked(L, k, loud=False):
    if len(L) < 2:
        if L:
            return L[0]
        else:
            return None
    pivot = L.peekLast()
    # uses the splitLinkedList function you write in part 1
    LT, GT, ET = splitLinkedList(L, pivot)
    if loud:
        print("Pivot:", pivot)
        print("Split lists:", LT, GT, ET)
    if k <= len(LT):
        return findKthLinked(LT, k, loud)
    elif k <= (len(LT) + len(ET)):
        return ET[0]
    else:
        k = k - (len(LT) + len(ET))
        return findKthLinked(GT, k, loud)

def findKth(L, k, keyFunc=identity):
    if len(L) < 2:
        if L:
            return L[0]
        else:
            return None
    mid = len(L)//2
    pivot = L[mid]
    (L1, L2, L3) = splitListKth(L, pivot, keyFunc)
    if k <= len(L1):
        return findKth(L1, k, keyFunc)
    elif k <= (len(L1) + len(L3)):
        return L3[0]
    else:
        k = k - (len(L1) + len(L3))
        return findKth(L2, k, keyFunc)

def splitListKth(L, pivot, keyFunc):
    L1 = [] #less than the pivot
    L2 = [] #greater than the pivot
    L3 = [] #equals the pivot
    for x in L:
        a, b = keyFunc(x), keyFunc(pivot) #a = keyFunc(x), b = keyFunc(pivot)
        if a < b:
            L1.append(x)
        elif a > b:
            L2.append(x)
        else:
            L3.append(x)
    return (L1, L2, L3)

L = LinkedList([13, 1, 5, 9, 11, 7])
# # print(quickSortInPlace(L, keyFunc = negative))
# y = findKthLinked(L, 6, True)
# print(y)
# # print("_____________________________________________________")
x = findKth(L, 1, negative)
print(x)
