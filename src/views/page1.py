import flet as ft

def Page1(page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def next_click(e):
        page.go('/page2')

    content =  ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
                ft.IconButton(ft.Icons.ADD, on_click=next_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
    )
    
    return content
