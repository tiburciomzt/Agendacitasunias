import tkinter as tk


def nick_gui():

    def obtener_nick():
        ans= nick.get()
        root.destroy()

    root = tk.Tk()
    root.title("Nick")

    nick = tk.StringVar()

    frame = tk.Frame(root)
    frame.grid(row=0, column=0, padx=5, pady=5)

    label_nick = tk.Label(frame, text="Inserte su nick y pulse en Listo!")
    label_nick.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="n")

    insert_nick = tk.Entry(frame, width=30, textvariable=nick)
    insert_nick.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    boton_nick = tk.Button(frame, text="Listo!", command=obtener_nick)
    boton_nick.grid(row=2, column=1, sticky="e", padx=5, pady=5)

    print(nick.get())
    root.mainloop()


if __name__ == "__main__":
    nick_gui()