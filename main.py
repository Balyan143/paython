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

    # Midabyada waxaan ka dhignay qoraal caadi ah sida "blue" si ay meel kasta uga shaqeeyaan
    title_text = ft.Text("Kusoo dhawaow App-ka! 👋", size=26, weight=ft.FontWeight.BOLD, color="blue")
    result_text = ft.Text("Guji batoonka hoose si aad casharka u soo dejiso", size=16)
    
    batoon_qoraal = ft.Text("Soo Deji Casharka 🌐", size=18, color="white")
    color_button = ft.ElevatedButton(
        content=batoon_qoraal, 
        bgcolor="blue",
        width=220,
        height=65
    )

    def fetch_data(e):
        title_text.value = "Wuu soo dejinayaa..."
        batoon_qoraal.value = "Sug..."
        page.update()
        
        try:
            req = urllib.request.Request(URL_ONLINE, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req, timeout=10)
            data = json.loads(response.read().decode('utf-8'))
            
            title_text.value = data.get("ciwaan", "Baro Midabyada Maanta!")
            batoon_qoraal.value = data.get("midabka_batoonka", "CAS")
            
            # Hubinta midabada iyadoo la isticmaalayo qoraal caadi ah
            midab = data.get("midabka_batoonka")
            if midab == "RED":
                color_button.bgcolor = "red"
            elif midab == "GREEN":
                color_button.bgcolor = "green"
            elif midab == "BLUE":
                color_button.bgcolor = "blue"
            else:
                color_button.bgcolor = "orange"
                
            def on_color_click(e):
                result_text.value = data.get("magaca_midabka", "Kani waa midab cusub!")
                page.update()
                
            color_button.on_click = on_color_click
            result_text.value = "Casharkii wuu yimid! Guji batoonka."
            
        except Exception as err:
            title_text.value = "Cillad Internet! ❌"
            batoon_qoraal.value = "Mar Kale Tijaabi"
            result_text.value = f"Hubi intarnet-kaaga."
            color_button.on_click = fetch_data
            
        page.update()

    color_button.on_click = fetch_data

    page.add(
        title_text,
        ft.Divider(height=30, color="transparent"),
        color_button,
        ft.Divider(height=20, color="transparent"),
        result_text
    )

ft.app(target=main)
