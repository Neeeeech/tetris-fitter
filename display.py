"""RETURNS PYGLET OBJECTS TO BE DRAWN FROM INPUT DATA"""

from pyglet import shapes


def color_gen(seed):
    return (seed * 107 + 10) % 256, (seed * 427 + 100) % 256, (seed * 97 + 194) % 256


def draw_grids(grid_length, batch):
    """draws divider and grid backgrounds"""
    increment = 400 / grid_length
    holder = [shapes.Line(480, 20, 480, 520, batch=batch, color=(255, 0, 0))]
    for i in range(0, int(grid_length) + 1):
        """Left Grid"""
        holder.append(shapes.Line(40 + increment * i, 70, 40 + increment * i, 470, batch=batch))
        holder.append(shapes.Line(40, 70 + increment * i, 440, 70 + increment * i, batch=batch))
        """Right Grid"""
        holder.append(shapes.Line(520 + increment * i, 70, 520 + increment * i, 470, batch=batch))
        holder.append(shapes.Line(520, 70 + increment * i, 920, 70 + increment * i, batch=batch))
    return holder


def draw_tiles(mat, batch, is_left, is_unicolor, is_white=False):
    holder = []
    grid_length = len(mat)
    increment = 400 / grid_length
    lbound_x = 40 if is_left else 520
    lbound_y = 470 - increment
    color = color_gen if not is_unicolor else (lambda a: (192,192,192)) if not is_white else (lambda a: (255,255,255))
    for y in range(grid_length):
        for x in range(grid_length):
            if mat[y][x] != 0:
                holder.append(shapes.Rectangle(lbound_x + x * increment,
                                               lbound_y - y * increment,
                                               increment, increment,
                                               color=color(mat[y][x]),
                                               batch=batch))
    return holder
