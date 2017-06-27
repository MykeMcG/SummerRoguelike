import libtcodpy as libtcod

class player(object):
    def __init__(self, pos_x, pos_y, background):
        self.__pos_x_prev = None
        self.__pos_y_prev = None
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__back  = background
   
    def draw(self, console):
        if self.__pos_x_prev != None and self.__pos_y_prev != None:
            libtcod.console_put_char(console, self.__pos_x_prev, self.__pos_y_prev, ' ', self.__back)
        libtcod.console_put_char(console, self.pos_x, self.pos_y, '@', self.__back)

    @property
    def pos_x(self):
        return self.__pos_x

    @pos_x.setter
    def pos_x(self, x):
        self.__pos_x_prev = self.pos_x
        self.__pos_y_prev = self.pos_y
        self.__pos_x = x

    @property
    def pos_y(self):
        return self.__pos_y

    @pos_y.setter
    def pos_y(self, y):
        self.__pos_x_prev = self.pos_x
        self.__pos_y_prev = self.pos_y
        self.__pos_y = y
