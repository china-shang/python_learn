#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

loop = asyncio.get_event_loop()


async def f():
    return True


async def ff():
    if(await f()):
        print("True")
loop.run_until_complete(ff())


class Root:
    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(), 'draw')


class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)

    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super().draw()


class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        print(type(color))
        super().__init__(**kwds)

    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()


cs = ColoredShape( color='blue', shapename='square')
cs.draw()
