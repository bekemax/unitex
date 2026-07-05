import flet as ft
from replace import replace

class mwb:
    def __new__(cls,message):
       instance = super().__new__(cls)
       instance.message = replace(message) 
       return ft.Row(controls=[ft.TextField(multiline=True,value=instance.message),
       ft.Button("Copy",on_click=instance.set_to_clipboard)])               
    
    async def set_to_clipboard(self):
        await ft.Clipboard().set(self.message)
    
def main(page: ft.Page):
    chat = ft.Column()
    new_message = ft.TextField(multiline=True)

    def send_click(e):
        chat.controls.append(mwb(new_message.value))
        new_message.value = ""

    page.add(
        chat,
        ft.Row(controls=[new_message, ft.Button("Convert", on_click=send_click)]),
    )

ft.run(main)