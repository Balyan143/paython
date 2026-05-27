import flet as ft
import urllib.request
import json

def main(page: ft.Page):
    page.title = "App-ka Carruurta (Online)"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Khadka tooska ah ee JSON-kaaga
    URL_ONLINE = "https://raw.githubusercontent.com/Balyan143/paython/main/casharada.json"

    title_text = ft.Text("Soo dejinaya casharka...", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
    result_text = ft.Text("Sug dhowr ilbiriqsi...", size=18)
    
    color_button = ft.ElevatedButton(
        text="Guji", 
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.GREY_400,
        width=220,
        height=65
    )

    def load_online_data():
        try:
            # Adeegsiga headers si GitHub u ogaado inuu yahay app dhab ah
            req = urllib.request.Request(
                URL_ONLINE, 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            response = urllib.request.urlopen(req, timeout=10)
            data = json.loads(response.read().decode('utf-8'))
            
            title_text.value = data.get("ciwaan", "Baro Midabyada Maanta!")
            color_button.text = data.get("midabka_batoonka", "CAS")
            
            if data.get("midabka_batoonka") == "RED":
                color_button.bgcolor = ft.Colors.RED
                
            def on_click_action(e):
                result_text.value = data.get("magaca_midabka", "Kani waa Midabka CAS!")
                page.update()
                
            color_button.on_click = on_click_action
            
        except Exception as err:
            title_text.value = "Cillad Internet! 🌐"
            color_button.text = "Tijaabi Mar Kale"
            result_text.value = f"Ma gari karo xogta: {str(err)}"
            
        page.update()

    page.add(
        title_text,
        ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
        color_button,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        result_text
    )

    load_online_data()

# Khadkan hoose wuxuu si toos ah Android ugu qasbayaa inuu shido Internet-ka!
ft.app(
    target=main,
    assets_dir="assets",
    web_renderer=ft.WebRenderer.HTML
)
