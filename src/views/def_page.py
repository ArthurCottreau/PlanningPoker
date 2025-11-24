import flet as ft

def defPage(page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER        
        
    content =  ft.Row(
            [
                ft.Text("This is an empty page !")
            ],
            alignment=ft.MainAxisAlignment.CENTER
    )

    page.go('/page1')

    return content
