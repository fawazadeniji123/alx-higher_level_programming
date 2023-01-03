class Rectangle:
  def __init__(self, width=0, height=0):
    self.width = width
    self.height = height

  @property
  def width(self):
    return self._width

  @width.setter
  def width(self, value):
    if not isinstance(value, int):
      raise TypeError("width must be an integer")
    if value < 0:
      raise ValueError("width must be >= 0")
    self._width = value

  @property
  def height(self):
    return self._height

  @height.setter
  def height(self, value):
    if not isinstance(value, int):
      raise TypeError("height must be an integer")
    if value < 0:
      raise ValueError("height must be >= 0")
    self._height = value

  def __dict__(self):
    return {'_Rectangle__width': self.width, '_Rectangle__height': self.height}
