class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.len = 0
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if len(self.array) == 0:
            self.array.append(x)
            return None
        remove = self.array.pop(-1)
        self.push(x)
        self.array.append(remove)
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.array.pop(-1)
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.array[-1] 
    
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.array) == 0



