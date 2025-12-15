import flet as ft

from misc.save_data import SaveData
from misc.tasks import Task

def PageTask(page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def add_name_clicked(e):
        if new_name.value:
            name = Task(new_name.value, name_delete)
            names.controls.append(name)
            new_name.value = ""
            new_name.focus()
            page.update()

    def name_delete(task):
        names.controls.remove(task)
        page.update()

    def save_tasks(e: ft.FilePickerResultEvent):
        mySD = SaveData()
        mySD.reset()
        
        name_list_length = len(names.controls)
        task_list_length = len(tasks.controls)

        if name_list_length and task_list_length:
            all_names = []
            all_tasks = {}
            nb = 0

            for name in names.controls:
                all_names.append(name.task_name)          
            mySD.set_element("users",all_names)

            for task in tasks.controls:
                all_tasks[nb]=task.task_name
                nb += 1
            mySD.set_element("tasks",all_tasks)
            mySD.set_element("gm_moyenne",gamemode.value)

            mySD.save_json(e.path)
            page.go('/')
        else:
            print("Tu ne peux pas avoir aucun utilisateur(s) ou aucune tache(s)")

    def click_save(e):
        file_picker.save_file()

    def add_clicked(e):
        if new_task.value:
            task = Task(new_task.value, task_delete)
            tasks.controls.append(task)
            new_task.value = ""
            new_task.focus()
            page.update()

    def task_delete(task):
        tasks.controls.remove(task)
        page.update()

    file_picker = ft.FilePicker(on_result=save_tasks)
    page.overlay.append(file_picker)

    new_name = ft.TextField(
        hint_text="Veuillez-entrer les noms d'utilisateurs", on_submit=add_name_clicked, expand=True
    )

    new_task = ft.TextField(
        hint_text="Veuillez-entrer les taches", on_submit=add_clicked, expand=True
    )

    gamemode = ft.Checkbox(label="Mode de jeu Moyenne", label_position=ft.LabelPosition.RIGHT, value=False)

    names = ft.Column()
    tasks = ft.Column()

    content = ft.Row(
        [
            ft.Container(
                ft.Column(
                    [
                        ft.Row(
                            [ft.Text(value="Nom d'utilisateur", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                new_name,
                                ft.FloatingActionButton(
                                    icon=ft.Icons.ADD, on_click=add_name_clicked
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            width=580
                        ),
                        ft.Column(
                            spacing=25,
                            controls=[
                                names
                            ],
                            width=580
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    scroll=ft.ScrollMode.ALWAYS
                ),
                width=400,
                height=500
            ),
            ft.Container(
                ft.Column(
                    [
                        ft.Row(
                            [ft.Text(value="Taches", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                new_task,
                                ft.FloatingActionButton(
                                    icon=ft.Icons.ADD, on_click=add_clicked
                                ),
                                ft.FloatingActionButton(
                                    icon=ft.Icons.DONE, on_click=click_save
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            width=580
                        ),
                        ft.Column(
                            spacing=25,
                            controls=[
                                tasks,
                                gamemode
                            ],
                            width=580
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    scroll=ft.ScrollMode.ALWAYS
                ),
                width=600,
                height=500
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )    
    
    return content
