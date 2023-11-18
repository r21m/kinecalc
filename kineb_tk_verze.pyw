import tkinter as tk
from tkinter import Menu, messagebox, Toplevel
from tkinter import Text, messagebox, simpledialog

# Proměnné pro písmo
font_label = ("Arial", 16)
font_entry = ("Arial", 16)
font_button = ("Arial", 16)
font_output = ("Arial", 16)

# Globální proměnné pro uchování hodnot
global_xkin = 0.0
global_zkin = 0.0

def vypocet():
    xkin_text = entry_xkin.get().replace(',', '.')
    zkin_text = entry_zkin.get().replace(',', '.')
    x1d_text = entry_x1d.get().replace(',', '.')
    x2d_text = entry_x2d.get().replace(',', '.')

    if not xkin_text or not zkin_text or not x1d_text or not x2d_text:
        vystup.config(text="Všechna pole musí být vyplněna.", font=font_output)
        return

    xkin = float(xkin_text)
    zkin = float(zkin_text)
    x1d = float(x1d_text)
    x2d = float(x2d_text)

    global global_xkin
    global global_zkin

    xkin2 = xkin + (x1d + x2d) / 2
    zkin2 = zkin + (x1d + x2d) / 2 - x2d

    global_xkin = xkin2
    global_zkin = zkin2

    vystup.config(text=f"xkin nový a střed stolu: {xkin2:.3f}\n zkin nový: {zkin2:.3f}", font=font_output, anchor="w")

    # Aktivuj tlačítko "Znovu" po úspěšném výpočtu
    reset_button.config(state=tk.NORMAL)

def znovu():
    entry_xkin.delete(0, tk.END)
    entry_zkin.delete(0, tk.END)
    entry_x1d.delete(0, tk.END)
    entry_x2d.delete(0, tk.END)

    entry_xkin.insert(0, str(global_xkin))
    entry_zkin.insert(0, str(global_zkin))

    # Neaktivuj tlačítko "Znovu" do té doby, než bude znovu stisknuto tlačítko "Vypočítat"
    reset_button.config(state=tk.DISABLED)

def o_programu():
    info = "KINECALC GPT pro o stůl\n\nAutor: Petr Novacek & chatGPT\nVerze: 20231811\nLicense: GNU GENERAL PUBLIC LICENSE Version 3.0"
    messagebox.showinfo("O programu", info)

def zavrit_okno():
    root.destroy()

# Vytvoření hlavního okna
root = tk.Tk()
root.title("KINECALC GPT pro o stůl")
root.geometry("400x350")
root.resizable(False, False)

# Vytvoření vstupních polí
entry_xkin = tk.Entry(root, width=10, font=font_entry)
entry_zkin = tk.Entry(root, width=10, font=font_entry)
entry_x1d = tk.Entry(root, width=10, font=font_entry)
entry_x2d = tk.Entry(root, width=10, font=font_entry)

# Vytvoření popisků pro vstupní pole
label_xkin = tk.Label(root, text="Hodnota Xkin:", font=font_label)
label_zkin = tk.Label(root, text="Hodnota Zkin:", font=font_label)
label_x1d = tk.Label(root, text="x1 delta z M41 do M42:", font=font_label)
label_x2d = tk.Label(root, text="x2 delta z M42 do M41:", font=font_label)

# Vytvoření tlačítka pro výpočet
calculate_button = tk.Button(root, text="Vypočítat", command=vypocet, font=font_button)

# Vytvoření tlačítka "Znovu"
reset_button = tk.Button(root, text="Znovu", command=znovu, font=font_button, state=tk.DISABLED)

# Vytvoření horní lišty s možností "O programu" a "Ukončit"
menu_bar = Menu(root)
root.config(menu=menu_bar)
menu_program = Menu(menu_bar)
menu_bar.add_cascade(label="Program", menu=menu_program)
menu_program.add_command(label="O programu", command=o_programu)
menu_program.add_separator()
menu_program.add_command(label="Ukončit", command=zavrit_okno)

# Vytvoření pole pro zobrazení výsledků
vystup = tk.Label(root, text="", font=font_output)

# Rozmístění prvků v okně
label_xkin.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_xkin.grid(row=0, column=1, padx=10, pady=5)
label_zkin.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_zkin.grid(row=1, column=1, padx=10, pady=5)
label_x1d.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_x1d.grid(row=2, column=1, padx=10, pady=5)
label_x2d.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_x2d.grid(row=3, column=1, padx=10, pady=5)
calculate_button.grid(row=4, column=0, pady=10)
reset_button.grid(row=4, column=1, pady=10)
vystup.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
