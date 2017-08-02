import textwrap
import libtcodpy as libtcod

# TODO: Change this class to just print a buffer every frame instead.
# TODO: Add MessageBuffer class

class MessagePanel:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lines = []

    def append(self, text, color=libtcod.white):
        new_msg_lines = textwrap.wrap(text, self.width)

        for line in new_msg_lines:
            # If the buffer is full, remove the first line to make room
            if len(self.lines) == self.height:
                del self.lines[0]
            self.lines.append((line, color))

    def render(self):
        con = libtcod.console_new(self.width, self.height)
        y = 1
        for (line, color) in self.lines:
            libtcod.console_set_default_foreground(con, color)
            libtcod.console_print_ex(con, 0, y, libtcod.BKGND_NONE,
                                     libtcod.LEFT, line)
            y += 1
        return con
