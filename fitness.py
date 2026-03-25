import tkinter as tk
from tkinter import ttk, filedialog
import json
import os


# Übungen Montag
plan_data = {
    "Montag": [
        "CAT COW POSE - Aufwärmen",
        "• 5 Runden langsam atmen (Rücken rund/hohl machen)",
        "• 30 Sekunden pro Übergang",
        "",
        "DECLINE SHOULDER PRESS - Schultern",
        "• Füße erhöht (Stuhl/Sofa), Hände schulterbreit",
        "• 3 Sätze x 10-12 Wiederholungen",
        "",
        "FRONT RAISES - Vordere Schultern",
        "• Arme gerade vorne heben (Wasserflaschen)",
        "• 3 Sätze x 12-15 Wiederholungen",
        "",
        "SIDE RAISES - Seitliche Schultern",
        "• Arme seitlich heben bis Schulterhöhe",
        "• 3 Sätze x 12-15 Wiederholungen",
        "",
        "SHOULDER PRESS - Alle Schultern",
        "• Arme über Kopf drücken",
        "• 3 Sätze x 10-12 Wiederholungen",
        "",
        "OVERHEAD TRICEP EXTENSION - Trizeps",
        "• Einarmig hinter Kopf strecken",
        "• 3 Sätze x 12 pro Arm",
        "",
        "DIPS - Trizeps/Brust",
        "• Stuhl/Kante benutzen, Ellenbogen eng",
        "• 3 Sätze x 8-12 Wiederholungen",
        "",
        "RUSSIAN TWIST - Schräge Bauchmuskeln",
        "• Sitzen, Füße anheben, drehen",
        "• 3 Sätze x 20 pro Seite",
        "",
        "SIDE BENDS - Seitliche Bauchmuskeln",
        "• Stehend seitlich neigen (Gewichte optional)",
        "• 3 Sätze x 15 pro Seite"
    ]
}

# JSON speichern
with open("uebungen.json", "w", encoding='utf-8') as f:
    json.dump(plan_data, f, ensure_ascii=False, indent=2)


# ÜBUNGEN A–Z MIT ANLEITUNGEN
UEBUNGEN_A_Z = {
    "A": {
        "name": "Kniebeugen (Squats)",
        "anleitung": (
            "KORREKTE AUSFÜHRUNG:\n\n"
            "1. Füße schulterbreit, Zehen leicht nach außen.\n"
            "2. Rücken gerade, Brust raus, Kopf in Verlängerung.\n"
            "3. Beuge die Knie, Po schieben nach hinten (nicht die Knie vor).\n"
            "4. Unterkörper senken, bis Oberschenkel etwa parallel zum Boden.\n"
            "5. Mit Oberschenkeln, Po und Waden wieder hochdrücken."
        )
    },
    "B": {
        "name": "Liegestütze (Push‑Ups)",
        "anleitung": (
            "KORREKTE AUSFÜHRUNG:\n\n"
            "1. Körper in einer Linie (Kopf, Hüfte, Fersen).\n"
            "2. Hände schulterbreit unter den Schultern.\n"
            "3. Beuge Arme, senke Brust Richtung Boden.\n"
            "4. Arme vollständig durchdrücken, aber Schultern nicht „einknicken“.\n"
        )
    },
    "C": {
        "name": "Crunches (Bauchmuskel)",
        "anleitung": (
            "KORREKTE AUSFÜHRUNG:\n\n"
            "1. Auf dem Rücken liegend, Knie gebeugt.\n"
            "2. Hände leicht hinter dem Kopf (nicht ins Genick ziehen).\n"
            "3. Schultern und obere Brust vom Boden heben.\n"
            "4. Bauchmuskulatur dabei gespannt halten, nicht mit dem Nacken ziehen.\n"
            "5. Langsam zurück zum Boden, Bauch immer leicht angespannt."
        )
    },
    "D": {
        "name": "Plank (Unterarmstütz)",
        "anleitung": (
            "KORREKTE AUSFÜHRUNG:\n\n"
            "1. Auf den Unterarmen liegend, Ellbogen unter Schultern.\n"
            "2. Körper in einer Linie, kein Hüfte‑Durchhängen, kein Hüfte‑Hochziehen.\n"
            "3. Bauch und Po leicht anspannen, Luft gleichmäßig atmen.\n"
            "4. Je nach Level 20–60 Sekunden halten."
        )
    }
}


# FUNKTIONEN: ÜBUNGEN A–Z FENSTER UND DETAIL‑ANLEITUNG

def oeffne_uebungen_az(root):
    az_window = tk.Toplevel(root)
    az_window.title("🏋️ Übungen A–Z")
    az_window.geometry("600x600")

    tk.Label(
        az_window,
        text="Ü b u n g e n   A – Z",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    canvas = tk.Canvas(az_window)
    scrollbar = tk.Scrollbar(az_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for buchstabe in sorted(UEBUNGEN_A_Z.keys()):
        uebung = UEBUNGEN_A_Z[buchstabe]
        frame = tk.Frame(scrollable_frame, pady=2)
        frame.pack(anchor="w", padx=10, fill="x")

        btn = tk.Button(
            frame,
            text=f"{buchstabe}) {uebung['name']}",
            font=("Arial", 12),
            anchor="w",
            command=lambda u=uebung: oeffne_uebungs_anleitung(root, u)
        )
        btn.pack(fill="x")


def oeffne_uebungs_anleitung(root, uebung):
    detail = tk.Toplevel(root)
    detail.title(f"Übung: {uebung['name']}")
    detail.geometry("550x450")

    tk.Label(
        detail,
        text=uebung["name"],
        font=("Arial", 16, "bold"),
    ).pack(pady=10)

    text = tk.Text(detail, wrap="word", font=("Arial", 12))
    text.insert("1.0", uebung["anleitung"])
    text.configure(state="disabled")
    text.pack(fill="both", expand=True, padx=10, pady=10)

    tk.Button(
        detail,
        text="🗙 Schließen",
        font=("Arial", 12),
        command=detail.destroy,
    ).pack(pady=10)


# +++ NEU: Ernährungsberater-Funktion +++

def oeffne_ernaehrungsberater(root):
    er_window = tk.Toplevel(root)
    er_window.title("😋 Ernährungsberater")
    er_window.geometry("600x500")

    tk.Label(
        er_window,
        text="Ernährungsberater",
        font=("Arial", 20, "bold")
    ).pack(pady=10)

    text = tk.Text(er_window, wrap="word", font=("Arial", 12))
    text.insert("1.0", """ERGEBNIS DES ERNÄHRUNGSBERATERS:

Gute Punkte:
• Ausreichend Wasser trinken ✓
• Viele Gemüse und Salat ✓

Korrigieren:
• Zu viel Zucker (Softdrinks, Süßigkeiten)
• Zu wenig Eiweiß (z.B. Hähnchen, Fisch, Käse, Ei)
• Zu wenig Ballaststoffe (Vollkorn, Hülsenfrüchte)

Tipps für bessere Ernährung:
1. 3 Mahlzeiten + 2 Snacks am Tag.
2. Jede Mahlzeit mit etwas Eiweiß.
3. Viel Wasser, wenig zuckerhaltige Getränke.
4. Zucker und Süßes nur in kleinen Mengen.""")
    text.configure(state="disabled")
    text.pack(fill="both", expand=True, padx=20, pady=10)

    tk.Button(
        er_window,
        text="schließen",
        command=er_window.destroy,
        bg="gray",
        fg="white",
        font=("Arial", 14),
        height=2
    ).pack(pady=20)


# HAUPT‑KLASSE
class FitnessApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fitness App")
        self.root.geometry("450x500")
        self.root.minsize(400, 400)

        self.tage = ["Montag"]
        self.hauptmenue()

    def hauptmenue(self):
        for w in self.root.winfo_children():
            w.destroy()

        tk.Label(
            self.root,
            text="WAHLE DEINEN TRAININGSTAG",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        # Scroll-Listbox
        listframe = tk.Frame(self.root)
        listframe.pack(pady=20, padx=40, fill="both", expand=True)

        scrollbar = tk.Scrollbar(listframe)
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(
            listframe,
            font=("Arial", 16),
            height=6,
            yscrollcommand=scrollbar.set,
            selectmode=tk.SINGLE
        )
        scrollbar.config(command=self.listbox.yview)

        for tag in self.tage:
            self.listbox.insert(tk.END, "Montag")

        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.select_set(0)

        # Buttons
        btnframe = tk.Frame(self.root)
        btnframe.pack(pady=20)

        tk.Button(
            btnframe,
            text="TRAINING STARTEN",
            command=self.training_fenster,
            font=("Arial", 16, "bold"),
            bg="#4CAF50",
            fg="white",
            height=2
        ).pack(pady=10)

        tk.Button(
            btnframe,
            text="FORM ANALYSE",
            command=self.form_analyse,
            font=("Arial", 16, "bold"),
            bg="#FF5722",
            fg="white",
            height=2
        ).pack(pady=10)

        # Übungen (A–Z) nur auf der Hauptseite
        tk.Button(
            btnframe,
            text="🏋️ Übungen (A–Z)",
            command=lambda: oeffne_uebungen_az(self.root),
            bg="#00aa00",
            fg="white",
            font=("Arial", 16, "bold"),
            height=2
        ).pack(pady=10)

        # Ernährungsberater-Button auf der Hauptseite
        tk.Button(
            btnframe,
            text="😋 Ernährungsberater",
            command=lambda: oeffne_ernaehrungsberater(self.root),
            bg="#FF9800",
            fg="white",
            font=("Arial", 16, "bold"),
            height=2
        ).pack(pady=10)

        tk.Button(
            btnframe,
            text="BEENDEN",
            command=self.root.quit,
            bg="#f44336",
            fg="white",
            font=("Arial", 14),
            height=2
        ).pack()

    def training_fenster(self):
        selection = self.listbox.curselection()
        if not selection:
            return
        tag = "Montag"

        # Neues Fenster
        plan_win = tk.Toplevel(self.root)
        plan_win.title(f"{tag} Training")
        plan_win.geometry("650x750")

        tk.Label(
            plan_win,
            text=f"{tag.upper()}",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        # Scrollbar-Text
        textframe = tk.Frame(plan_win)
        textframe.pack(fill="both", expand=True, padx=20, pady=10)

        scrollbar = tk.Scrollbar(textframe)
        scrollbar.pack(side="right", fill="y")

        text = tk.Text(
            textframe,
            wrap="word",
            font=("Consolas", 13),
            yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=text.yview)

        uebungen = plan_data["Montag"]
        for line in uebungen:
            text.insert(tk.END, line + "\n")
        text.config(state="disabled")

        text.pack(fill="both", expand=True)

        tk.Button(
            plan_win,
            text="ZURÜCK",
            command=plan_win.destroy,
            bg="#2196F3",
            fg="white",
            font=("Arial", 16)
        ).pack(pady=20)

    def form_analyse(self):
        for w in self.root.winfo_children():
            w.destroy()

        tk.Label(
            self.root,
            text="FORM ANALYSE - Lade Foto",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        foto_path = tk.StringVar()

        def foto_laden():
            datei = filedialog.askopenfilename(
                title="Fitness‑Foto auswählen (Seitenansicht)",
                filetypes=[("Bilder", "*.jpg *.png *.jpeg")]
            )
            if datei:
                foto_path.set(datei)
                tk.Label(
                    self.root,
                    text=f"{os.path.basename(datei)} geladen!",
                    fg="green",
                    font=("Arial", 14)
                ).pack(pady=5)

        # Button: FOTO LADEN
        tk.Button(
            self.root,
            text="FOTO LADEN",
            command=foto_laden,
            bg="#2196F3",
            fg="white",
            font=("Arial", 16, "bold"),
            height=2
        ).pack(pady=10)

        # Button ZURÜCK (immer sichtbar, auch vor Analyse)
        tk.Button(
            self.root,
            text="ZURÜCK",
            command=self.hauptmenue,
            bg="gray",
            fg="white",
            font=("Arial", 16, "bold"),
            height=2
        ).pack(pady=10)

        def analysieren():
            if not foto_path.get():
                tk.Label(
                    self.root,
                    text="Lade zuerst ein Foto!",
                    fg="red",
                    font=("Arial", 16)
                ).pack(pady=10)

                # ZURÜCK-Button auch bei Fehler
                tk.Button(
                    self.root,
                    text="ZURÜCK",
                    command=self.hauptmenue,
                    bg="gray",
                    fg="white",
                    font=("Arial", 16, "bold"),
                    height=2
                ).pack(pady=10)
                return

            analyse = """FORM ANALYSE ERGEBNIS:

Gute Punkte:
• Schultern symmetrisch ✓
• Becken stabil ✓

Korrigieren:
• Rücken leicht gekrümmt → Gerader halten!
• Knie nach innen → Knie auseinander drücken!

Training Fokus:
1. PLANK - 3x60s
2. DEADLIFT - Rücken gerade
3. SHOULDER DISLOCATIONS - Mobilität

SCORE: 82/100"""

            for w in self.root.winfo_children():
                w.destroy()

            tk.Label(
                self.root,
                text="ANALYSE FERTIG!",
                font=("Arial", 22, "bold"),
                fg="green"
            ).pack(pady=20)

            text_widget = tk.Text(
                self.root,
                wrap="word",
                font=("Consolas", 12),
                height=20,
                width=60
            )
            text_widget.pack(pady=10, padx=20, fill="both", expand=True)

            text_widget.insert("1.0", analyse)
            text_widget.config(state="disabled")

            tk.Button(
                self.root,
                text="HAUPTMENÜ",
                command=self.hauptmenue,
                bg="#2196F3",
                fg="white",
                font=("Arial", 16, "bold"),
                height=2
            ).pack(pady=20)

            # Jetzt auch ZURÜCK in der Analyse
            tk.Button(
                self.root,
                text="ZURÜCK",
                command=self.hauptmenue,
                bg="gray",
                fg="white",
                font=("Arial", 16),
                height=2
            ).pack(pady=10)

        # Button ANALYSE
        tk.Button(
            self.root,
            text="ANALYSE",
            command=analysieren,
            bg="#FF5722",
            fg="white",
            font=("Arial", 18, "bold"),
            height=2
        ).pack(pady=30)

    def run(self):
        self.root.mainloop()


# APP STARTEN
FitnessApp().run()
