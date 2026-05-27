from flet import *

def main(page: Page):
    page.title = "Flet Login Page"
    
    # --- Habka saxda ah ee loo qasbo cabbirka nidaamka cusub ---
    page.window.width = 390
    page.window.height = 740
    page.window.resizable = False  # Si aan gacanta loogu weyneyn karin
    
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    # Meelaha qoraalka laga gelinayo (Input Fields)
    username_input = TextField(
        label="Magaca isticmaalaha (Username)", 
        width=320
    )
    
    password_input = TextField(
        label="Erayga Sirta ah (Password)", 
        width=320, 
        password=True, 
        can_reveal_password=True
    )

    message_text = Text(value="", color="green", size=14)

    def login_click(e):
        if username_input.value == "" or password_input.value == "":
            message_text.value = "Fadlan buuxi dhamaan meelaha banaan!"
            message_text.color = "red"
        else:
            message_text.value = f"Ku soo dhowaw, {username_input.value}!"
            message_text.color = "green"
        page.update()

    login_button = ElevatedButton(
        content=Text("Login"), 
        on_click=login_click, 
        width=150
    )

    # Qaybta weyn ee Login-ka
    login_card = Card(
        content=Container(
            content=Column(
                controls=[
                    Text("Ku soo Dhawaw", size=22, weight=FontWeight.BOLD),
                    Text("Geli xogtaada", size=12, color="grey"),
                    Divider(),
                    username_input,
                    password_input,
                    Container(height=10),
                    login_button,
                    message_text
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            padding=20,
            width=340,
        )
    )

    page.add(login_card)
    page.update() # Aad u muhiim ah si cabbirka daaqadda uu u hirgalo

# Amarka caadiga ah ee shaqaynaya khalad la'aan
app(target=main)