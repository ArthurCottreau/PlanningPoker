import flet as ft

from misc.save_data import SaveData

def PageGame(page):
    page.bgcolor = ft.Colors.WHITE

    task_text = ft.Text(
        value="Êtes-vous prêts?",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_GREY_900
    )

    user_name = ft.Text(
        value="",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_GREY_900
    )

    mySD = SaveData()
    names = []
    tasks = {}
    user_turn = 0
    task_turn = 0
    first_turn = 0 # Pour mode de jeu moyenne
    results = {}
    turn_results = {}

    # Suite de Fibonacci et options spéciales
    poker_values = ["0", "1", "2", "3", "5", "8", "13", "21", "34", "55", "89", "☕"]

    # Texte pour afficher le résultat sélectionné
    result_text = ft.Text(
        value="Veuillez choisir une estimation", # Veuillez choisir une estimation
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_GREY_900
    )

    # Variable pour suivre la carte actuellement sélectionnée
    current_selection = None


    def save_game(e: ft.FilePickerResultEvent):
        mySD.save_json(e.path)

    file_picker = ft.FilePicker(on_result=save_game)
    page.overlay.append(file_picker)

    def end_game(e):
        nonlocal current_selection

        # Désélectionne la carte lorsque le choix du joueur est confirmé
        current_selection.bgcolor = ft.Colors.WHITE
        current_selection.border = ft.border.all(2, ft.Colors.BLUE_200)
        current_selection.scale = 1.0
        current_selection = None
        result_text.value = "Veuillez choisir une estimation"

        user_name.value = ""
        task_text.value = "Êtes-vous prêts?"

        file_picker.save_file()
        page.session.clear()
        page.go('/')       

    def next_turn(e):
        nonlocal names
        nonlocal tasks
        nonlocal user_turn
        nonlocal task_turn
        nonlocal first_turn
        nonlocal results
        nonlocal turn_results
        nonlocal current_selection

        if current_selection:
            # Pour mettre en place la partie
            if not page.session.get("game_started"):
                names = mySD.get_element("users")
                tasks = mySD.get_element("tasks")
                user_turn = len(names) # Pour le tour préparation
                task_turn = 0
                first_turn = 0
                results = {}
                turn_results = {}

                if mySD.get_element("results"):
                    task_turn = len(mySD.get_element("results"))-1
                    turn_results = mySD.get_element("results")
                    turn_results.pop(str(task_turn), None)

            user_turn += 1
            results[user_name.value] = current_selection.data

            if user_turn >= len(names):
                
                if page.session.get("game_started"):

                    # Pour les modes de jeux
                    if mySD.get_element("gm_moyenne"):
                        # Un 1er tour d'unanimité - mode de jeu moyenne
                        if first_turn == 0:
                            if len(set(results.values())) != 1:
                                task_turn -= 1
                            else:
                                task_turn -= 1
                                first_turn += 1
                        else:
                            first_turn = 0

                            sum_result = 0
                            for value in results.values():
                                sum_result += int(value)
                            
                            turn_results[task_turn - 1] = sum_result / len(results)
                    else:
                        # Pour l'unanimité - mode de jeu strict
                        if len(set(results.values())) != 1:
                            task_turn -= 1
                        else:
                            turn_results[task_turn - 1] = results[user_name.value]
                    
                    mySD.set_element("results",turn_results)

                # Mise à jour des tours pour les taches
                if task_turn < len(tasks):
                    task_turn += 1
                    user_turn = 0
                    
                    # Vérifie si tout le monde a sélectionner le café
                    if page.session.get("game_started"):
                        if results[names[user_turn]] == "☕":
                            if len(set(results.values())) == 1:
                                task_turn -= 1
                                end_game(e)
                                return

                    user_name.value = names[user_turn]
                    task_text.value = "Tache : " + tasks[str(task_turn - 1)]

                    page.session.set("game_started", 1)
                else:
                    end_game(e)

                results = {}
            else:
                # Mise à jour des tours pour les joueurs
                user_name.value = names[user_turn]

        # Désélectionne la carte lorsque le choix du joueur est confirmé
        current_selection.bgcolor = ft.Colors.WHITE
        current_selection.border = ft.border.all(2, ft.Colors.BLUE_200)
        current_selection.scale = 1.0
        current_selection = None
        result_text.value = "Veuillez choisir une estimation"

        page.update()

    def card_clicked(e):
        nonlocal current_selection
        clicked_container = e.control
        
        # 1. Réinitialiser le style de la carte précédente (si elle existe)
        if current_selection:
            current_selection.bgcolor = ft.Colors.WHITE
            current_selection.border = ft.border.all(2, ft.Colors.BLUE_200)
            current_selection.scale = 1.0
            current_selection.update()

        # 2. Définir le style de la carte cliquée (mise en évidence)
        clicked_container.bgcolor = ft.Colors.BLUE_50
        clicked_container.border = ft.border.all(3, ft.Colors.BLUE_700)
        clicked_container.scale = 1.1 # Léger agrandissement lors du clic
        clicked_container.update()

        # 3. Mettre à jour l'état global et le texte
        current_selection = clicked_container
        result_text.value = f"Points d'estimation : {clicked_container.data}"
        page.update()

    # Construire la liste des cartes
    cards = []
    for value in poker_values:
        # Utiliser un Container pour simuler une carte de poker
        card = ft.Container(
            content=ft.Text(
                value=value, 
                size=24, 
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK87
            ),
            data=value,  # Stocker la valeur représentée par la carte
            width=80,    # Largeur de la carte
            height=120,  # Hauteur de la carte
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(2, ft.Colors.BLUE_200),
            border_radius=ft.border_radius.all(10),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=ft.Colors.BLUE_GREY_100,
                offset=ft.Offset(0, 2),
            ),
            # Configuration de l'animation
            animate_scale=ft.Animation(300, ft.AnimationCurve.BOUNCE_OUT),
            animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
            # Événement de clic
            on_click=card_clicked,
            # Le curseur devient une main au survol
            ink=True,
        )
        cards.append(card)

    # Utiliser Row pour un alignement horizontal
    cards_row = ft.Row(
        controls=cards,
        wrap=False, # False signifie pas de retour à la ligne, garde une seule ligne
        scroll=ft.ScrollMode.AUTO, # Permet le défilement horizontal
        spacing=20, # Espacement entre les cartes
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Conteneur avec barre de défilement (ajout de remplissage pour l'esthétique)
    layout_container = ft.Container(
        content=cards_row,
        padding=ft.padding.symmetric(vertical=20),
    )

    content = ft.Column(
        [
            task_text,
            user_name,
            ft.Divider(height=25, color=ft.Colors.TRANSPARENT), # Espace vide
            result_text,
            ft.Divider(height=25, color=ft.Colors.TRANSPARENT), # Espace vide
            layout_container,
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT), # Espace vide
            ft.CupertinoButton(
                content=ft.Row(
                    [
                        ft.Icon(
                            name=ft.Icons.DONE,
                            color=ft.Colors.WHITE
                        ),
                        ft.Text(
                            value="Confirmer selection",
                            color=ft.Colors.WHITE
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                bgcolor=ft.Colors.GREEN_700,
                opacity_on_click=0.3,
                on_click=next_turn,
                width=page.width / 3
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    
    return content
