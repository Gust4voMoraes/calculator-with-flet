import flet as ft

def main(page: ft.page):
    page.title = "Flet Calculator"
    page.window_height = 400
    page.window_width = 300
    page.window_resizable = False
    page.bgcolor = "#5F0F40"

    #function to read keys
    def keyboard(e):
        data = e.control.data

        if data in ["1","2","3","4","5","6","7","8","9","0",".","+","-","*","/","(",")"]:
                txt.value = str(txt.value) + str(data)
                page.update()
        
        #functionality to equal(=) button
        if data == "=":
             txt.value = str(eval(txt.value))
             page.update()
        
        #functionality to backspace(<) button
        if data == "e": #convert the text field to a list and remove the last item, then join list items and put it on text field
             st = list(txt.value)
             st.pop()
             txt.value = "".join(map(str,st))
             page.update()
        
        #functionality to clear(C) button
        if data == "c":
             txt.value = ""
             page.update()

    txt = ft.TextField(
        read_only=True,
        border_color="#E0AED0",
        border_width=3,
        text_style=ft.TextStyle(size=30,color="#FFFFFF")
    )
    page.add(txt)

    button_e = ft.ElevatedButton(
            text="<", bgcolor="#820300", color="#FFFFFF", data="e", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_po = ft.ElevatedButton(
            text="(", bgcolor="#820300", color="#FFFFFF", data="(", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_pc = ft.ElevatedButton(
            text=")", bgcolor="#820300", color="#FFFFFF", data=")", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_division = ft.ElevatedButton(
            text="÷", bgcolor="#820300", color="#FFFFFF", data="/", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r1 = ft.Row(
        controls=[button_e,button_po,button_pc,button_division],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    
    button_7 = ft.ElevatedButton(
            text="7", bgcolor="#E0AED0", color="#FFFFFF", data="7", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_8 = ft.ElevatedButton(
            text="8", bgcolor="#E0AED0", color="#FFFFFF", data="8", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_9 = ft.ElevatedButton(
            text="9", bgcolor="#E0AED0", color="#FFFFFF", data="9", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_multi = ft.ElevatedButton(
            text="x", bgcolor="#820300", color="#FFFFFF", data="*", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r2 = ft.Row(
        controls=[button_7,button_8,button_9,button_multi],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    button_4 = ft.ElevatedButton(
            text="4", bgcolor="#E0AED0", color="#FFFFFF", data="4", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_5 = ft.ElevatedButton(
            text="5", bgcolor="#E0AED0", color="#FFFFFF", data="5", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_6 = ft.ElevatedButton(
            text="6", bgcolor="#E0AED0", color="#FFFFFF", data="6", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_sub = ft.ElevatedButton(
            text="-", bgcolor="#820300", color="#FFFFFF", data="-", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r3 = ft.Row(
        controls=[button_4,button_5,button_6,button_sub],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    button_1 = ft.ElevatedButton(
            text="1", bgcolor="#E0AED0", color="#FFFFFF", data="1", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_2 = ft.ElevatedButton(
            text="2", bgcolor="#E0AED0", color="#FFFFFF", data="2", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_3 = ft.ElevatedButton(
            text="3", bgcolor="#E0AED0", color="#FFFFFF", data="3", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_add = ft.ElevatedButton(
            text="+", bgcolor="#820300", color="#FFFFFF", data="+", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r4 = ft.Row(
        controls=[button_1,button_2,button_3,button_add],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    button_c = ft.ElevatedButton(
            text="C", bgcolor="#AF2655", color="#FFFFFF", data="c", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_0 = ft.ElevatedButton(
            text="0", bgcolor="#E0AED0", color="#FFFFFF", data="0", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_dot = ft.ElevatedButton(
            text=".", bgcolor="#AF2655", color="#FFFFFF", data=".", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    button_eq = ft.ElevatedButton(
            text="=", bgcolor="#820300", color="#FFFFFF", data="=", on_click=keyboard,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r5 = ft.Row(
        controls=[button_c,button_0,button_dot,button_eq],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    page.add(r1,r2,r3,r4,r5)

ft.app(target=main)