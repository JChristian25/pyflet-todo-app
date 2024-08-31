new_note_overlay = ft.Container(
        visible=False,  # Initially hidden
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
            alignment=ft.MainAxisAlignment.CENTER,  # Centers content vertically within the column
            vertical_alignment=ft.MainAxisAlignment.CENTER  # Centers content horizontally within the row
        ),
        alignment=ft.alignment.center
    )