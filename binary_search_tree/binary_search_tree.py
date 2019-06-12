class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value is None:
      self.value = value
    elif value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target > self.value:
      return self.right.contains(target) if self.right is not None else False
    else:
      return self.left.contains(target) if self.left is not None else False

  def get_max(self):
    return self.value if self.right is None else self.right.get_max()

  def for_each(self, cb):
    cb(self.value)
    if self.left is not None:
      self.left.for_each(cb)
    if self.right is not None:
      self.right.for_each(cb)