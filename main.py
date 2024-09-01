import flet as ft
import retrieve as rt
import write as wr

def mainWindow(page: ft.Page):

    # Set window size to mimic a mobile device
    page.window_width = 375   # Width in pixels (e.g., iPhone 8 width)
    page.window_height = 667  # Height in pixels (e.g., iPhone 8 height)
    page.window_resizable = False  # Prevent window resizing
    page.window_maximizable = False  # Prevent window maximization
    page.window_minimizable = False  # Prevent window minimization

    title_input = ft.TextField(label="Title", width=300)
    text_input = ft.TextField(label="Text", width=300, multiline=True)

    # Reference to the card to update later
    card_ref = ft.Ref[ft.Card]()

    # Initialize the overlay with a reference to control visibility later
    new_note_overlay = ft.Container(
        visible=False,  # Initially hidden
        content=ft.Container(
            content=ft.Row(
                controls=[
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text("Add New Note", weight=ft.FontWeight.BOLD, size=20),
                                    title_input,
                                    text_input,
                                    ft.Row(
                                        controls=[
                                            ft.ElevatedButton("Add Note", on_click=lambda e: add_note()),
                                            ft.ElevatedButton("Cancel", on_click=lambda e: toggle_overlay(False))
                                        ],
                                        alignment=ft.MainAxisAlignment.END
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            padding=ft.Padding(20, 0, 20, 0),
                        ),
                        height=400,
                        width=350,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER  # Centers content vertically within the row
            ),
            alignment=ft.alignment.center  # Centers the content both horizontally and vertically
        ),
        alignment=ft.alignment.center,  # Centers the entire overlay container on the screen
    )

    def toggle_overlay(show):
        new_note_overlay.visible = show
        page.update()

    def btnClicked(e):
        toggle_overlay(True)

    def add_note():
        note_title = title_input.value
        note_text = text_input.value
        wr.getValue(note_title, note_text)  # Assuming this function updates the JSON file
        toggle_overlay(False)  # Hide the overlay after adding the note
        
        # Update the card content
        updated_card = update_card()
        card_ref.current.content = updated_card.content
        page.update()

    def update_card():
        title, text = retrieve_from_file()
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            title,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD,
                            size=20
                        ),
                        ft.Text(
                            text,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center,
                width=400,
                padding=ft.Padding(10, 10, 10, 10)
            )
        )

    def retrieve_from_file():
        title, text = rt.return_info()  # Retrieves title and text from return_info function in retrieve module
        return title, text

    # Initial card creation
    card = update_card()
    card_ref.current = card

    # Add main content and overlay to the page
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.FloatingActionButton(icon=ft.icons.ADD, on_click=btnClicked)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    card
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center
        ),
        new_note_overlay
    )

ft.app(target=mainWindow)
