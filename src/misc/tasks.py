import flet as ft

class Task(ft.Column):
    """
    @author COTTREAU Arthur
    @class Task
    @brief Classe pour chaque tâches sur la page pour générer le JSON
    """
    def __init__(self, task_name, task_delete):
        """
        @brief Constructeur de la classe
        @param task_name: Texte pour chaque tâche
        @param task_delete: Contient la fonction pour supprimer l'objet de la page
        """
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete
        self.edit_name = ft.TextField(expand=1)

        self.display_task = ft.Text(
            value=self.task_name,
            weight=ft.FontWeight.BOLD
        )

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            tooltip="Modifiez une tache",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.Icons.DELETE_OUTLINE,
                            tooltip="Supprimez une tache",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="Mettre a jour une taches",
                    on_click=self.save_clicked,
                ),
            ],
        )

        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, e):
        """
        @brief Fonction pour modifier une tache
        """
        self.edit_name.value = self.display_task.value
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        """
        @brief Fonction pour sauvegarder une tache
        """
        self.display_task.value = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        """
        @brief Fonction pour supprimer une tache
        """
        self.task_delete(self)