from dataclasses import make_dataclass, field


def draw(self):
    return f"window: {(self.width, self.height)}; color: {self.color}"


Window = make_dataclass(
    'Window',
    [
        ('width', int),
        ('height', int),
        ('color', str, field(default='gray', init=False, compare=False)),
    ],
    namespace={'draw': draw}
)

wnd = Window(width=100, height=20)