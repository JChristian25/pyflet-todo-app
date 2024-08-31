import flet as ft
import retrieve as rt
import write as wr

def mainWindow(page: ft.Page):
    title, text = retrieve()

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
                                    ft.TextField(label="Title", width=300),
                                    ft.TextField(label="Text", width=300, multiline=True),
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
        alignment=ft.alignment.center,  # Centers the entire overlay container on the screen\
    )

    def toggle_overlay(show):
        """Toggle the visibility of the overlay."""
        new_note_overlay.visible = show
        page.update()

    def btnClicked(e):
        """Handle FloatingActionButton click to show overlay."""
        toggle_overlay(True)

    def add_note():
        """Handle the addition of a new note."""
        # You can add logic here to handle the new note addition
        toggle_overlay(False)  # Hide the overlay after adding the note

    # Add main content and overlay to the page
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.FloatingActionButton(icon=ft.icons.ADD, on_click=btnClicked)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER  # Aligns the Row's contents horizontally
                    ),
                    card(title=title, text=text)
                ],
                alignment=ft.MainAxisAlignment.CENTER  # Centers the contents of the column
            ),
            alignment=ft.alignment.center
        ),
        new_note_overlay  # Add overlay to the page
    )

def retrieve():
    title, text = rt.return_info()
    return title, text

def card(title=None, text=None):
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        title,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,  # Aligns text horizontally within its container
                        size=20
                    ),
                    ft.Text(
                        text,
                        text_align=ft.TextAlign.CENTER
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centers content vertically within the column
                horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Centers content horizontally within the column
            ),
            alignment=ft.alignment.center,  # Centers the entire container within the card
            width=400,
            padding=ft.Padding(10, 10, 10, 10)
        )
    )

ft.app(target=mainWindow)
