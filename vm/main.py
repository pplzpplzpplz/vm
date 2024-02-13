import flet as ft


def main(page: ft.Page):
    page.title = 'Voice Memo Mate'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.padding = 100  # Add padding for centering



    #file picker
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.add(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.Text(
                    "Voice Memo Mate", 
                    color="blue", 
                    size=26, 
                    weight="bold"
                    )
            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ]
        )
    )


ft.app(main)
