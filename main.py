import flet as ft
from replace import replace

def main(page: ft.Page):
    chat = ft.Column()
    new_message = ft.TextField(multiline=True)
    text_to_copy = ft.TextField(multiline=True)


    def send_click(e):
        chat.controls.append(ft.Row(controls=[ft.Text(replace(new_message.value)),ft.Button("Copy", on_click=set_to_clipboard)]))
        new_message.value = ""
        text_to_copy.value = ""

    async def set_to_clipboard():
        await ft.Clipboard().set(text_to_copy.value)
        text_to_copy.value = ""
        page.show_dialog(ft.SnackBar("Text copied to clipboard"))
        
    page.add(
        chat,
        ft.Row(controls=[new_message, ft.Button("Convert", on_click=send_click)]),
    )


ft.run(main)