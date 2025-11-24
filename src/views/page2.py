import flet as ft

def Page2(page):

    def next_click(e):
        page.go('/page1')

    content =  ft.Row(
            [
                ft.Text("Hello, you're on page 2 !"),
                ft.IconButton(ft.Icons.ADD, on_click=next_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER
    )
    
    return content
