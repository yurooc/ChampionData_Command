from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
import opgg
import time
import random

def table():
    table_upper = Table()
    table_upper.add_column("Rank")
    table_upper.add_column("Champion")
    table_upper.add_column("Tier")
    table_upper.add_column("Win Rate")
    table_upper.add_column("Pick Rate")
    table_upper.add_column("Ban Rate")
    a = opgg.Data().opgg()
    for i in a:
        table_upper.add_row(i.group('id'),i.group('name'),'T'+i.group('tier'),i.group('win')+'%',i.group('pick')+'%',i.group('ban')+'%')

    return table_upper
def layout_():
    layout = Layout()
    layout.split_column(
        Layout(Panel(table())),
        Layout(name="lower")
    )
    layout["lower"].split_row(
        Layout(Panel('left')),
        Layout(Panel('right')),
    )

    print(layout)

layout_()