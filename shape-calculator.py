class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return (self.height * self.width)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):

        #assert self.width <= 50, "Too big for picture"

        if self.width > 50:
          #print("Too big for picture.")
          return "Too big for picture."

        picture = ""

        for number in range(0, self.height):
            picture_str = ""
            picture_str += "*" * self.width + "\n"
            picture += picture_str
        
      
        return picture
            
    def get_amount_inside(self, shape):

        home_object_area = self.get_area()
        guest_object = shape.get_area() 

        return home_object_area//guest_object

    def set_height(self, new_height):
        self.height = new_height

    def set_width(self, new_width):
        self.width = new_width


    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):

    def __init__(self, width, height=None):
        
        self.width = width

        if height is None:
            self.height = width
        
    def set_side(self, width, height=None):

        self.width = width
        self.height = width

    def __str__(self):
        return "Square(side=" + str(self.width) + ")" 