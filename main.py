import flet as ft
from replace import replace


    
def main(page: ft.Page):
    
          
  tf1 = ft.TextField(label="Type here",multiline=True,max_lines=5)  
  
  tf2 = ft.TextField(label="Result",multiline=True,max_lines=5)

  async def set_to_clipboard(e):
        await ft.Clipboard().set(tf2.value)
  
  def on_click1(e):
      tf2.value = replace(tf1.value) 
      
  but1 = ft.Button("Convert",on_click=on_click1)

  but2 = ft.Button("Copy",on_click=set_to_clipboard)  
  
  buttons = ft.Row(expand=True,controls=[but1,but2])

  col = ft.Column(spacing=10, controls=[tf1,tf2,buttons],
  alignment=ft.CrossAxisAlignment.CENTER)
    

  page.window.height=700
  page.window.width=400      
  page.window.resizeable=False
  
  page.add(col)  

ft.run(main)