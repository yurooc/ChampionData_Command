from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
import opgg,opgg2
import time

def table_left():
    table_left = Table()
    table_left.add_column("Rank")
    table_left.add_column("Champion")
    table_left.add_column("Tier")
    table_left.add_column("Win Rate")
    table_left.add_column("Pick Rate")
    table_left.add_column("Ban Rate")
    table_left.style = 'blue'
    table_left.expand = True
    table_left.highlight = True
    iter_ = str(input("请输入段位"))
    position_ = str(input("请输入位置"))
    a = opgg.Data(iter_, position_).opgg()
    for i in a:
        table_left.add_row(i.group('id'), i.group('name'), 'T' + i.group('tier'), i.group('win') + '%',
                           i.group('pick') + '%', i.group('ban') + '%')
    return table_left
def table_up():
    table_upper = Table()
    table_upper.add_column("name")
    table_upper.add_column("team")
    table_upper.add_column("iter")
    table_upper.add_column("ID")
    table_upper.add_column("championname")
    b = opgg2.opgg2()
    for j in b:
        table_upper.add_row(j.group('id_name'),j.group('team_name'),j.group('iter'),j.group('id'),j.group('champion_name'))
    return table_upper


def layout_():
    layout = Layout()
    layout.split_row(
        Layout(Panel(table_left())),
        Layout(name="right")
    )
    layout["right"].split_column(
        Layout(Panel(table_up())),
        Layout(Panel("lower"))
    )

    print(layout)


if __name__ == '__main__':
    layout_()