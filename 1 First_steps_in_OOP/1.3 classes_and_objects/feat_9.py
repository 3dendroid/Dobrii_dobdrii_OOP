class Figure:
    type_fig: str = 'ellipse'
    color: str = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'

fig1.__delattr__('color')
print(*fig1.__dict__)
# print (*fig1.__dict__.keys())
