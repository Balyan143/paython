import flet as ft
import urllib.request
import json

def main(page: ft.Page):
    page.title = "App-ka Carruurta"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Link-ga rasmiga ah ee GitHub-kaaga
    URL_ONLINE = "https://raw.githubusercontent.com/Balyan143/paython/main/casharada.json"

    title_text = ft.Text("Kusoo dhawaow App-ka! 👋", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
    result_text = ft.Text("Guji batoonka hoose si aad casharka u soo dejiso", size=16)
    
    # Batoonkan wuxuu marka hore soo dejinayaa xogta, ka dibna wuxuu noqonayaa midabkii
    color_button = ft.ElevatedButton(
        text="Soo Deji Casharka 🌐", 
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLUE,
        width=220,
        height=65
    )

    def fetch_data(e):
        title_text.value = "Wuu soo dejinayaa..."
        color_button.text = "Sug..."
        page.update()
        
        try:
            req = urllib.request.Request(URL_ONLINE, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req, timeout=10)
            data = json.loads(response.read().decode('utf-8'))
            
            title_text.value = data.get("ciwaan", "Baro Midabyada Maanta!")
            color_button.text = data.get("midabka_batoonka", "CAS")
            
            # Hubinta midabada
            midab = data.get("midabka_batoonka")
            if midab == "RED":
                color_button.bgcolor = ft.Colors.RED
            elif midab == "GREEN":
                color_button.bgcolor = ft.Colors.GREEN
            elif midab == "BLUE":
                color_button.bgcolor = ft.Colors.BLUE
            else:
                color_button.bgcolor = ft.Colors.ORANGE
                
            def on_color_click(e):
                result_text.value = data.get("magaca_midabka", "Kani waa midab cusub!")
                page.update()
                
            # Ku xir batoonka ficilka cusub ee casharka
            color_button.on_click = on_color_click
            result_text.value = "Casharkii wuu yimid! Guji batoonka."
            
        except Exception as err:
            title_text.value = "Cillad Internet! ❌"
            color_button.text = "Mar Kale Tijaabi"
            result_text.value = f"Hubi intarnet-kaaga ama koodhka JSON."
            # Haddii uu khaldamo, dib ugu celi nidaamkii soo dejinta
            color_button.on_click = fetch_data
            
        page.update()

    # Batoonku marka hore wuxuu wadaa shaqada soo dejinta
    color_button.on_click = fetch_data

    page.add(
        title_text,
        ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
        color_button,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        result_text
    )

ft.app(target=main)
