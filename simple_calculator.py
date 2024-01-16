import flet as ft

def main(page: ft.page):
    page.title = "Calculator"
    page.window_height = 400
    page.window_width = 300
    page.bgcolor = "#78184a"

    txt = ft.TextField(
        #read_only=True,
        border_color="#000000",
        text_style=ft.TextStyle(size=30,color="#FFFFFF")
    )
    page.add(txt)

    button_e = ft.ElevatedButton(
            text="<", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_po = ft.ElevatedButton(
            text="(", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_pc = ft.ElevatedButton(
            text=")", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_division = ft.ElevatedButton(
            text="÷", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r1 = ft.Row(
        controls=[button_e,button_po,button_pc,button_division],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    
    button_7 = ft.ElevatedButton(
            text="7", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_8 = ft.ElevatedButton(
            text="8", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_9 = ft.ElevatedButton(
            text="9", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_multi = ft.ElevatedButton(
            text="x", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r2 = ft.Row(
        controls=[button_7,button_8,button_9,button_multi],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    button_4 = ft.ElevatedButton(
            text="4", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_5 = ft.ElevatedButton(
            text="5", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_6 = ft.ElevatedButton(
            text="6", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_sub = ft.ElevatedButton(
            text="-", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r3 = ft.Row(
        controls=[button_4,button_5,button_6,button_sub],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    button_1 = ft.ElevatedButton(
            text="1", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_2 = ft.ElevatedButton(
            text="2", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_3 = ft.ElevatedButton(
            text="3", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_add = ft.ElevatedButton(
            text="+", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r4 = ft.Row(
        controls=[button_1,button_2,button_3,button_add],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    button_c = ft.ElevatedButton(
            text="C", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_0 = ft.ElevatedButton(
            text="0", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_dot = ft.ElevatedButton(
            text=".", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_eq = ft.ElevatedButton(
            text="=", bgcolor="#000000", color="#FFFFFF",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r5 = ft.Row(
        controls=[button_c,button_0,button_dot,button_eq],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    page.add(r1,r2,r3,r4,r5)

ft.app(target=main)