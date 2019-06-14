class Queue:
  def __init__(self):
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    return self.storage.append(item)
  
  def dequeue(self):
    if self.storage:
      return self.storage.pop(0)

  def len(self):
    return len(self.storage)

# I decided to use a list here because we are only adding and removing
# to the end, making the list the easiest option