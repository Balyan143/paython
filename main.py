import flet as ft
import json
import threading

def main(page: ft.Page):
    page.title = "Quiz & Video App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Link-ga rasmiga ah ee GitHub-kaaga
    URL_ONLINE = "https://raw.githubusercontent.com/Balyan143/paython/main/casharada.json"

    # Title text
    title_text = ft.Text("Quiz & Video App 🎬", size=26, weight=ft.FontWeight.BOLD, color="blue")
    
    # Video player component
    video_player = ft.Video(
        src="",
        width=350,
        height=200,
        autoplay=False,
        playback_rate=1.0,
        muted=False,
        visible=False
    )

    # Quiz container elements
    question_text = ft.Text("", size=18, weight=ft.FontWeight.BOLD, color="black", text_align=ft.TextAlign.CENTER)
    
    # Answer buttons
    button_1 = ft.ElevatedButton(text="", width=300, height=50, bgcolor="blue", color="white")
    button_2 = ft.ElevatedButton(text="", width=300, height=50, bgcolor="blue", color="white")
    button_3 = ft.ElevatedButton(text="", width=300, height=50, bgcolor="blue", color="white")
    
    # Result text
    result_text = ft.Text("", size=16, color="black", text_align=ft.TextAlign.CENTER)
    
    # Status text
    status_text = ft.Text("Casharka wuu soo dejinayaa...", size=14, color="gray")

    # Store quiz data
    current_quiz_data = {}

    def check_answer(button_text):
        """Check if the clicked answer is correct"""
        correct_answer = current_quiz_data.get("jawaabta_saxda_ah", "")
        
        if button_text == correct_answer:
            result_text.value = "Haa! Waad ku guulaysatay! 🎉"
            result_text.color = "green"
        else:
            result_text.value = "Mar kale tijaabi! 👍"
            result_text.color = "red"
        
        page.update()

    def on_button_1_click(e):
        check_answer(button_1.text)

    def on_button_2_click(e):
        check_answer(button_2.text)

    def on_button_3_click(e):
        check_answer(button_3.text)

    button_1.on_click = on_button_1_click
    button_2.on_click = on_button_2_click
    button_3.on_click = on_button_3_click

    def fetch_data_sync():
        """Fetch quiz data in a separate thread to prevent UI freezing"""
        try:
            status_text.value = "Wuu soo dejinayaa..."
            page.update()
            
            # Use requests library which works better on Android
            try:
                import requests
                response = requests.get(URL_ONLINE, timeout=10)
                response.raise_for_status()
                data = response.json()
            except ImportError:
                # Fallback to urllib if requests not available
                import urllib.request
                req = urllib.request.Request(URL_ONLINE, headers={'User-Agent': 'Mozilla/5.0'})
                response = urllib.request.urlopen(req, timeout=10)
                data = json.loads(response.read().decode('utf-8'))
            
            # Store quiz data globally
            nonlocal current_quiz_data
            current_quiz_data = data
            
            # Update UI with fetched data
            title_text.value = data.get("ciwaan", "Quiz & Video App 🎬")
            question_text.value = data.get("suuaal", "Suaalo: Midiiddaan maxay tahay?")
            
            # Update answer buttons with dynamic text
            button_1.text = data.get("batoon_1", "Option 1")
            button_2.text = data.get("batoon_2", "Option 2")
            button_3.text = data.get("batoon_3", "Option 3")
            
            # Load video from JSON if available
            video_link = data.get("video_link", "")
            if video_link:
                video_player.src = video_link
                video_player.visible = True
            else:
                video_player.visible = False
            
            result_text.value = "Guji jawaabta saxda ah!"
            result_text.color = "black"
            status_text.value = "Casharkii wuu yimid! 📚"
            
        except Exception as err:
            title_text.value = "Cillad Internet! ❌"
            question_text.value = "Cillad ayaa dhacday"
            button_1.text = "Mar Kale Tijaabi"
            button_2.text = ""
            button_3.text = ""
            result_text.value = f"Hubi intarnet-kaaga: {str(err)}"
            result_text.color = "red"
            video_player.visible = False
            status_text.value = "Cillad: Internet ayaa la xiriyahay"
            print(f"Error: {err}")  # For debugging
            
        page.update()

    def fetch_data(e):
        """Button click handler - runs fetch in background thread"""
        thread = threading.Thread(target=fetch_data_sync, daemon=True)
        thread.start()

    # Load data button
    load_button = ft.ElevatedButton(
        text="Soo Deji Casharka 🌐",
        width=220,
        height=65,
        bgcolor="blue",
        color="white",
        on_click=fetch_data
    )

    # Quiz container with all elements
    quiz_container = ft.Column(
        controls=[
            ft.Divider(height=10, color="transparent"),
            question_text,
            ft.Divider(height=15, color="transparent"),
            button_1,
            ft.Divider(height=10, color="transparent"),
            button_2,
            ft.Divider(height=10, color="transparent"),
            button_3,
            ft.Divider(height=15, color="transparent"),
            result_text,
        ],
        visible=False,
        spacing=5
    )

    def on_load_button_click(e):
        """Show quiz container when loading data"""
        quiz_container.visible = True
        fetch_data(e)

    load_button.on_click = on_load_button_click

    page.add(
        title_text,
        ft.Divider(height=20, color="transparent"),
        load_button,
        ft.Divider(height=20, color="transparent"),
        video_player,
        ft.Divider(height=20, color="transparent"),
        quiz_container,
        ft.Divider(height=10, color="transparent"),
        status_text
    )

ft.app(target=main)
