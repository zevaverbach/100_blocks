from collections import namedtuple

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from config import config, colors

Base = declarative_base()

engine = create_engine('sqlite:///boards.db')
session = scoped_session(sessionmaker(bind=engine))



class Board(Base):

    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    layout = Column(String(config['num_squares'] * 2), nullable=False)
    palette = Column(String(400), nullable=False)

    def __repr__(self):
        return f'<Layout> name: {self.name} {self.layout}'

    def update(self, layout):
        self.layout = layout
        session.commit()

    @property
    def color_list(self):
        return get_colors_from_palette(self.palette)

    @property
    def color_num_dict(self):
        return get_color_num_dict(self.color_list)


def get_boards(**kwargs):
    return session.query(Board).filter_by(**kwargs).all()


def get_board(**kwargs):
    one = get_boards(**kwargs)
    if len(one) > 0:
        return one[0]


def create_board(name, layout, colors):
    new_board = Board(name=name,
                      layout=layout,
                      palette=prep_colors_for_table(colors))

    session.add(new_board)
    session.commit()
    return new_board


def get_colors_from_palette(a_palette: str):
    parsed_colors = []
    palette_list = a_palette.split('#')[1:]
    for color in palette_list:
        if color[0].islower():
            parsed_colors.append(color)
        else:
            parsed_colors.append('#' + color)
    return parsed_colors


def get_color_num_dict(color_list):
    return {color: str(idx + 1).zfill(2) 
            for idx, color in enumerate(color_list)}


def prep_colors_for_table(some_colors):
    palette = ''
    for color in some_colors:
        if not color.startswith('#'):
            color = '#' + color
        palette += color
    return palette


def update_base_table():
    base_board = get_board()
    base_board.palette = ''.join(colors)
    session.commit()


base_board = get_board(name='') or create_board('', '00' * num_squares, colors)

# each number is represented by a two-digit integer string
color_num_dict = get_color_num_dict(colors)
