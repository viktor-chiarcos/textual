#!/bin/env python3
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label
import random,sys

class App(App):
    """Eine einfache Textual-Anwendung."""
    
    # Tastatur-Shortcuts am unteren Bildschirmrand definieren
    BINDINGS = [("d", "toggle_dark", "Dark Mode umschalten")]

    def compose(self) -> ComposeResult:
        """Hier werden die UI-Komponenten (Widgets) definiert."""
        
        yield Header()
        yield Label("Dies ist eine Wort-Auspuck-App. ")
        yield Button("Wort auspucken", variant="primary")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event-Handler, der auf den Button-Klick reagiert."""
        def NotifyContentText(randomchoice):
            if randomchoice: return random.choice(["Hallo","Guten Tag","Hi"])
            else: return "Das Programm hat die Reaktion nicht erlaubt!"
        self.notify(NotifyContentText(True))

if __name__ == "__main__":
    app = App()
    app.run()
