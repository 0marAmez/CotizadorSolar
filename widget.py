import tkinter as tk
import openpyxl
from PIL import Image, ImageTk
from datetime import date
from openpyxl.styles import Font
from  solar import PanelSolar


def load_and_resize_image(image_path, width, height):
    # Load the image
    image = Image.open(image_path)

    # Resize the image
    image = image.resize((width, height), Image.LANCZOS)

    # Convert the image to Tkinter format
    tk_image = ImageTk.PhotoImage(image)

    return tk_image

def create_rectangle_at_top(widget, width, height, x1, y1, x2, y2, rectangle_color):
    canvas = tk.Canvas(widget, width=width, height=height,bg="white",highlightthickness=0)
    canvas.pack()
    canvas.create_rectangle(x1, y1, x2, y2, fill=rectangle_color,outline="")

def on_button_click():
    cliente = entry1.get()
    direccion = entry3.get()
    numero_de_servicio = entry4.get()
    vendedor = entry5.get()
    promedio_kw = entry6.get()

    workbook = openpyxl.load_workbook("template/SolarEnergyTemplate.xlsx")
    worksheet = workbook.active

    paneles =  PanelSolar(float(promedio_kw))
    paneles.calcular_paneles()
    paneles.info_inversor()

    primernombre = cliente.split()
    worksheet['F9'] = 'Aguascalientes, Ags  '+ str(date.today())
    worksheet['C12'] = cliente
    worksheet['C13'] = direccion
    worksheet['I13'] = numero_de_servicio

    worksheet['D22'] = promedio_kw + " kwh/bm"
    worksheet['D23'] = str(paneles.capacidad_instalar)+" kwp"
    produccion = 0.0
    produccion = paneles.cantidad_de_paneles*550
    produccion = produccion/1000
    produccion = produccion*5
    produccion = produccion*60
    worksheet['D24'] = str(int(produccion))+" kwh/bm"


    worksheet['F28'] = paneles.cantidad_de_paneles
    worksheet['C31'] = "Inversor GROWATT "+paneles.modelo_inversor
    worksheet['F31'] = paneles.cantidad_inversores


    worksheet['B47'] = "Lic "+vendedor


    bold_font = Font(bold=True)
    worksheet['D22'].font = bold_font
    worksheet['D23'].font = bold_font
    worksheet['D24'].font = bold_font
    worksheet['B47'].font = bold_font


    new_file_name = f"{primernombre[0]+str(date.today())}_cotizacion.xlsx"
    cotizacion = 'cotizaciones/' +new_file_name

    workbook.save(cotizacion)
    workbook.close()


def on_option_selected(selected_option):
    print("Selected Option:", selected_option)
    

if __name__ == "__main__":

    # Root Widget
    root = tk.Tk()
    root.resizable(False, False)  # Disable both horizontal and vertical resizing
    root.configure(bg="#FCD12A")
    root.geometry("700x600")
    create_rectangle_at_top(root, 700, 110, 201, 0, 700, 100, "white")

    text_label1 = tk.Label(root, text="COTIZADOR", bg="white", font=("Arial", 18, "bold"), fg="#B2BEB5")
    text_label1.place(x=550, y=75)  # Set the position of the label




    # Image Label
    image_path = "images/solar.jpg"
    width, height = 200, 100
    tk_image = load_and_resize_image(image_path, width, height)
    # Create a label to display the image
    label = tk.Label(root, image=tk_image, bg="white")
    label.place(x=0 ,y=0)  # Set the label's coordinates



    # Create the input box (Nombre del recibo)
    text_label2 = tk.Label(root, text="Nombre del recibo", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label2.place(x=35, y=130)  # Set the position of the label
    entry1 = tk.Entry(root,bg="white",highlightthickness=0, relief=tk.FLAT,fg="black",width=30)
    entry1.place(x=15, y=160)


    # Create the input box (Correo)
    text_label3 = tk.Label(root, text="Correo", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label3.place(x=355, y=130)  # Set the position of the label
    entry2 = tk.Entry(root,bg="white",highlightthickness=0, relief=tk.FLAT,fg="black",width=30)
    entry2.place(x=300, y=160)


    # Create the input box (Direccion)
    text_label4 = tk.Label(root, text="Direccion", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label4.place(x=65, y=200)  # Set the position of the label
    entry3 = tk.Entry(root,bg="white",highlightthickness=0, relief=tk.FLAT,fg="black",width=30)
    entry3.place(x=15, y=230)


    # Create the input box (Numero De Servicio)
    text_label5 = tk.Label(root, text="No. de Servicio", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label5.place(x=335, y=200)  # Set the position of the label
    entry4 = tk.Entry(root,bg="white",highlightthickness=0, relief=tk.FLAT,fg="black",width=30)
    entry4.place(x=300, y=230)



    # Create the input box (Vendedor)
    text_label6 = tk.Label(root, text="Vendedor", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label6.place(x=65, y=270)  # Set the position of the label
    entry5 = tk.Entry(root,bg="white",highlightthickness=0, relief=tk.FLAT,fg="black",width=30)
    entry5.place(x=15, y=300)


    # Create the input box (Opciones)
    text_label7 = tk.Label(root, text="Seleccione una Opcion", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label7.place(x=315, y=270)  # Set the position of the label
    options = ["01", "PBDT", "DAC", "GDMTO"]
    selected_option = tk.StringVar(root)
    selected_option.set(options[0])  # Set the default selected option
    option_menu = tk.OptionMenu(root, selected_option, *options, command=on_option_selected)
    option_menu.config(width=15, anchor="center", bg="white", fg="black")  # Set background and text color of the menu
    option_menu["menu"].config(bg="white", fg="black")  # Set background and text color of the dropdown menu
    option_menu.place(x=300, y=300, width=200)



    # Create the input box (Promedio Bimestral)
    text_label8 = tk.Label(root, text="Promedio Bimestral", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label8.place(x=35, y=340)  # Set the position of the label
    entry6 = tk.Entry(root,bg="white",highlightthickness=0, relief=tk.FLAT,fg="black",width=30)
    entry6.place(x=15, y=370)


    # Create the input box (?)
    text_label9 = tk.Label(root, text="Random", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label9.place(x=355, y=340)  # Set the position of the label
    entry7 = tk.Entry(root,bg="white",highlightthickness=0, relief=tk.FLAT,fg="black",width=30)
    entry7.place(x=300, y=370)

    text_label10 = tk.Label(root, text="Nota del vendedor", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label10.place(x=195, y=410)  # Set the position of the label
    entry8 = tk.Text(root, bg="white",highlightthickness=0 ,relief=tk.FLAT,fg="black", width=30, height=5)  # Adjust the height as needed
    entry8.place(x=150, y=430)


    # Create a button to read the input and print it
    button = tk.Button(root, bg="#D3D3D3", text="Submit", command=on_button_click, highlightbackground="#FCD12A",font=("Arial", 12, "bold"))
    button.place(x=550, y=500,width=100, height=40)


    root.mainloop()
