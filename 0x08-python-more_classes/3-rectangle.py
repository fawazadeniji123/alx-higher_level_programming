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

  # Public instance method: def area(self): that returns the rectangle area
  def area(self):
    return self.width * self.height

  # Public instance method: def perimeter(self): that returns the rectangle perimeter:
  # if width or height is equal to 0, perimeter is equal to 0
  def perimeter(self):
    if self.width == 0 or self.height == 0:
      return 0
      
    return (self.width * 2) + (self.height * 2)

  def __repr__(self):
    return f'''
    ##########
    ##########
    ##########

    {self.__class__}
    '''

  def __str__(self):
    return f'''
    Area: {self.area()} - Perimeter: {self.perimeter()}
    ##
    ##
    ##
    ##
    {self.__class__}
    '''

  def __dict__(self):
    return {'_Rectangle__width': self.width, '_Rectangle__height': self.height}


rect = Rectangle(2,6)
print(rect)
print(repr(rect))