import flet as ft
import requests

def main(page: ft.Page):
    page.title = "App-ka Carruurta (Online)"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 1. Khadka tooska ah ee JSON-kaaga (Kani waa link-gii saxda ahaa ee galkaaga)
    URL_ONLINE = "https://raw.githubusercontent.com/Balyan143/paython/main/casharada.json"

    # Sameynta meelaha qoraalka iyo batoonka ee shaashadda ku yaal
    title_text = ft.Text("Soo dejinyaya casharka...", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
    result_text = ft.Text("Sug dhowr ilbiriqsi...", size=18)
    
    # Batoonka weyn ee midabka yeelan doona
    color_button = ft.ElevatedButton(
        text="Guji", 
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.GREY_400,
        width=220,
        height=65
    )

    # 2. Shaqada internet-ka wax ka soo akhrinaysa
    def load_online_data():
        try:
            # Sii wadashada internet-ka
            response = requests.get(URL_ONLINE, timeout=5)
            data = response.json() # Aqoonsiga qaabka JSON-ka
            
            # Soo bixinta xogta gudaha JSON-ka ku jirtay
            title_text.value = data.get("ciwaan", "Baro Midabyada Maanta! 🎨")
            color_button.text = data.get("midabka_batoonka", "CAS")
            
            # Beddelidda midabka batoonka si waafaqsan waxa online-ka ku jira
            if data.get("midabka_batoonka") == "RED":
                color_button.bgcolor = ft.Colors.RED
                
            # Shaqada dhacaysa marka batoonka la riixo (soo bandhigidda macnaha midabka)
            def on_click_action(e):
                result_text.value = data.get("magaca_midabka", "Kani waa Midabka CAS! ❤️")
                page.update()
                
            color_button.on_click = on_click_action
            
        except Exception as err:
            # Haddii talefanku uusan internet lahayn, kani waa casharka caadiga ah
            title_text.value = "Ku soo dhowow App-ka! 👶"
            color_button.text = "Tijaabi mar kale"
            result_text.value = "Fadlan shid internet-ka si aad casharka u aragto."
            
        page.update()

    # Ku darista walxaha shaashadda talefanka
    page.add(
        title_text,
        ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
        color_button,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        result_text
    )

    # Kicinta shaqada internet-ka isla marka uu app-ku furmo
    load_online_data()

ft.app(target=main)
