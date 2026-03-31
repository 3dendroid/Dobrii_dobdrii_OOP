from dataclasses import dataclass, field, InitVar


@dataclass
class FontData:
    name: str
    size: float
    color: int = field(compare=False, default=0)
    type_font: str = field(default=None)
    monotype: InitVar[bool] = field(compare=False, default=False)

    def __post_init__(self, monotype):
        if not monotype:
            self.type_font = "regular"


font = FontData(name="Tahoma", size=22)