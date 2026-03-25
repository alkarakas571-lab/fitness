import tkinter as tk
from datetime import datetime
import os, json

profil = "profil.json"
gewichte = "gewicht.txt"

root = tk.Tk()
root.title("Gewicht")
root.geometry("380x550")

def profil_pruefen():
    return os.path.exists(profil)

def neues_profil():
    for w in root.winfo_children(): w.destroy()
    
    tk.Label(root, text="👤 PROFIL", font=("Arial", 20, "bold")).pack(pady=20)
    
    tk.Label(root, text="Name:").pack(pady=5)
    name = tk.Entry(root, font=("Arial", 16))
    name.pack(pady=5)
    name.insert(0, "Ali")
    
    tk.Label(root, text="Alter:").pack(pady=10)
    alter = tk.Entry(root, font=("Arial", 16))
    alter.pack(pady=5)
    alter.insert(0, "30")
    
    tk.Label(root, text="Startgewicht:").pack(pady=20)
    start_slider = tk.Scale(root, from_=40, to=150, resolution=0.1, orient="horizontal", length=250)
    start_slider.set(85.0)
    start_slider.pack(pady=10)
    start_label = tk.Label(root, text="85.0 kg", font=("Arial", 20, "bold"))
    start_label.pack()
    
    def start_update(*args):
        start_label.config(text=f"{start_slider.get():.1f} kg")
    start_slider.config(command=start_update)
    
    tk.Label(root, text="🎯 Zielgewicht:", font=("Arial", 16, "bold")).pack(pady=(30,10))
    ziel_slider = tk.Scale(root, from_=40, to=150, resolution=0.1, orient="horizontal", length=250)
    ziel_slider.set(75.0)
    ziel_slider.pack(pady=10)
    ziel_label = tk.Label(root, text="75.0 kg", font=("Arial", 20, "bold"), fg="orange")
    ziel_label.pack()
    
    def ziel_update(*args):
        ziel_label.config(text=f"{ziel_slider.get():.1f} kg")
    ziel_slider.config(command=ziel_update)
    
    def profil_ok():
        daten = {
            "name": name.get(),
            "alter": alter.get(),
            "startgewicht": start_slider.get(),
            "zielgewicht": ziel_slider.get()
        }
        with open(profil, "w") as f:
            json.dump(daten, f)
        with open(gewichte, "a") as f:
            f.write(f"{datetime.now().strftime('%H:%M')},{start_slider.get():.1f}\n")
        normaler_modus()
    
    tk.Button(root, text="✅ PROFIL OK", command=profil_ok, 
              bg="green", fg="white", font=("Arial", 16), height=2).pack(pady=30)

def normaler_modus():
    for w in root.winfo_children(): w.destroy()
    
    with open(profil) as f:
        info = json.load(f)
    
    ziel = info.get('zielgewicht', 75.0)
    
    # Header
    tk.Label(root, text=f"👋 {info['name']} ({info['alter']})", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(root, text=f"🎯 Ziel: {ziel}kg", font=("Arial", 14), fg="orange").pack(pady=5)
    
    # Tägliches Gewicht
    tk.Label(root, text="📊 Gewicht heute:", font=("Arial", 14)).pack(pady=20)
    wert = tk.DoubleVar(value=80.0)
    anzeige = tk.Label(root, text="80.0 kg", font=("Arial", 28, "bold"))
    anzeige.pack(pady=10)
    
    slider = tk.Scale(root, from_=40, to=150, resolution=0.1, orient="horizontal", 
                      length=280, variable=wert, font=("Arial", 12))
    slider.pack(pady=10)
    
    info_label = tk.Label(root, text="", font=("Arial", 16))
    info_label.pack(pady=10)
    
    # 🎯 NEU: Zielgewicht ÄNDERN Button
    def ziel_aendern():
        for w in root.winfo_children(): w.destroy()
        tk.Label(root, text="🎯 Zielgewicht ändern", font=("Arial", 20, "bold")).pack(pady=30)
        
        ziel_neu_slider = tk.Scale(root, from_=40, to=150, resolution=0.1, orient="horizontal", length=280)
        ziel_neu_slider.set(ziel)
        ziel_neu_slider.pack(pady=20)
        ziel_neu_label = tk.Label(root, text=f"{ziel} kg", font=("Arial", 28, "bold"), fg="orange")
        ziel_neu_label.pack(pady=10)
        
        def ziel_update_neu(*args):
            ziel_neu_label.config(text=f"{ziel_neu_slider.get():.1f} kg")
        ziel_neu_slider.config(command=ziel_update_neu)
        
        def ziel_speichern():
            info['zielgewicht'] = ziel_neu_slider.get()
            with open(profil, "w") as f:
                json.dump(info, f)
            normaler_modus()
        
        tk.Button(root, text="✅ Ziel speichern", command=ziel_speichern,
                  bg="#FF9800", fg="white", font=("Arial", 16), height=2).pack(pady=20)
        tk.Button(root, text="❌ Zurück", command=normaler_modus,
                  bg="gray", fg="white", font=("Arial", 16), height=2).pack(pady=10)
    
    def update():
        w = round(wert.get(), 1)
        anzeige.config(text=f"{w} kg")
        
        # 🎯 Farbe nach ZIELGEWICHT!
        diff_ziel = w - ziel
        if diff_ziel > 0:
            info_label.config(text=f"+{diff_ziel}kg (über Ziel)", fg="red")
        elif diff_ziel < 0:
            info_label.config(text=f"{diff_ziel}kg (unter Ziel)", fg="green")
        else:
            info_label.config(text="✅ ZIEL ERREICHT!", fg="gold")
    
    wert.trace("w", lambda x,y,z: update())
    update()
    
    def speichern():
        with open(gewichte, "a") as f:
            f.write(f"{datetime.now().strftime('%H:%M')},{wert.get():.1f}\n")
        tk.Label(root, text="✅ GESPEICHERT! (schliesst in 1s)", 
                font=("Arial", 14), fg="green").pack(pady=10)
        root.after(1000, root.quit)
    
    # 2 Buttons nebeneinander
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)
    
    tk.Button(button_frame, text="💾 Wiegen speichern", command=speichern,
              bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), height=2).pack(side="left", padx=10)
    tk.Button(button_frame, text="🎯 Ziel ändern", command=ziel_aendern,
              bg="#FF9800", fg="white", font=("Arial", 14, "bold"), height=2).pack(side="left", padx=10)

if profil_pruefen():
    normaler_modus()
else:
    neues_profil()

root.mainloop()
