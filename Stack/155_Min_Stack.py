class MinStack(object):

def __init__(self):
    self.arr = []
    self.mini = []

def push(self, val):
    """
    :type val: int
    :rtype: None
    """
    self.arr.append(val)

    if not self.mini or val <= self.mini[-1]:
        self.mini.append(val)


def pop(self):
    """
    :rtype: None
    """

    if self.arr:
        if self.arr[-1] == self.mini[-1]:
            self.mini.pop()
        self.arr.pop()


def top(self):
    """
    :rtype: int
    """
    return self.arr[-1] if self.arr else None



def getMin(self):
    """
    :rtype: int
    """
    return self.mini[-1] if self.mini else None
