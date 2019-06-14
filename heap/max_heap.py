class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    return self._bubble_up(self.get_size()-1)

  def delete(self):
    if not self.storage:
      return False
    if self.get_size() == 1:
      return self.storage.pop()
    self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
    temp = self.storage.pop()
    self._sift_down(0)
    return temp
    

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    p = (index - 1) // 2

    if index <= 0:
      return
    
    elif self.storage[index] > self.storage[p]:
      self.storage[index], self.storage[p] = self.storage[p], self.storage[index]
      self._bubble_up(p)


  def _sift_down(self, index):
    l = (index * 2) + 1
    r = (index * 2) + 2
    target = index

    if self.get_size() > l and self.storage[target] < self.storage[l]:
      target = l
    if self.get_size() > r and self.storage[target] < self.storage[r]:
      target = r
    if target != index:
      self.storage[index], self.storage[target] = self.storage[target], self.storage[index]
      self._sift_down(target)