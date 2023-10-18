import tkinter as tk
import openpyxl
import matplotlib  
from PIL import Image, ImageTk
from datetime import date
from openpyxl.styles import Font
from  solar import PanelSolar

# Create a dictionary to store the entry widgets
entry_widgets = {}


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


def create_label_and_entry(root, label_text, entry_bg, entry_fg, entry_width, label_x, label_y,entry_x,entry_y):
    text_label = tk.Label(root, text=label_text, bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label.place(x=label_x, y=label_y)

    entry = tk.Entry(root, bg=entry_bg, highlightthickness=0, relief=tk.FLAT, fg=entry_fg, width=entry_width)
    entry.place(x=entry_x, y=entry_y)  

    # Store a reference to the entry widget in the dictionary
    entry_widgets[label_text] = entry

def open_promedio_bimestral_window():
    # Create a new window
    promedio_window = tk.Toplevel(root)

    # Create labels and entries in the new window
    create_label_and_entry(promedio_window, "Label 1", "white", "black", 30, 15, 15, 15, 50)
    create_label_and_entry(promedio_window, "Label 2", "white", "black", 30, 15, 60, 15, 95)
    create_label_and_entry(promedio_window, "Label 3", "white", "black", 30, 15, 105, 15, 140)

    # Create a button to close the new window
    close_button = tk.Button(promedio_window, text="Close", command=promedio_window.destroy)
    close_button.place(x=15, y=175)

def on_button_click():
    # Saca los valores del widget
    cliente = entry_widgets["Nombre del recibo"].get()
    print(cliente)
    # direccion = entry3.get()
    # numero_de_servicio = entry4.get()
    # vendedor = entry5.get()
    # promedios_kw = entry6.get()

    #Separa el promedio y para calcular el grafo
    # split_list = promedios_kw.split(',')
    # float_array = [float(num) for num in split_list]
    # promedio = sum(float_array) / len(float_array)



    # workbook = openpyxl.load_workbook("template/SolarEnergyTemplate.xlsx")
    # worksheet = workbook.active

    # paneles =  PanelSolar(promedio)
    # paneles.calcular_paneles()
    # paneles.info_inversor()

    # primernombre = cliente.split()
    # worksheet['F9'] = 'Aguascalientes, Ags  '+ str(date.today())
    # worksheet['C12'] = cliente
    # worksheet['C13'] = direccion
    # worksheet['I13'] = numero_de_servicio

    # worksheet['D22'] = str(promedio) + " kwh/bm"
    # worksheet['D23'] = str(paneles.capacidad_instalar)+" kwp"
    # produccion = 0.0
    # produccion = paneles.cantidad_de_paneles*550
    # produccion = produccion/1000
    # produccion = produccion*5
    # produccion = produccion*60
    # worksheet['D24'] = str(int(produccion))+" kwh/bm"


    # worksheet['F28'] = paneles.cantidad_de_paneles
    # worksheet['C31'] = "Inversor GROWATT "+paneles.modelo_inversor
    # worksheet['F31'] = paneles.cantidad_inversores


    # worksheet['B47'] = "Lic "+vendedor


    # bold_font = Font(bold=True)
    # worksheet['D22'].font = bold_font
    # worksheet['D23'].font = bold_font
    # worksheet['D24'].font = bold_font
    # worksheet['B47'].font = bold_font


    # new_file_name = f"{primernombre[0]+str(date.today())}_cotizacion.xlsx"
    # cotizacion = 'cotizaciones/' +new_file_name

    # workbook.save(cotizacion)
    # workbook.close()


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

    # Nombre en el recibo 
    create_label_and_entry(root, "Nombre del recibo", "white", "black", 35, 45, 130, 15, 160)
    # Direccion
    create_label_and_entry(root, "Direccion", "white", "black", 35, 365, 130, 300, 160)
    # No. de Cotizacion
    create_label_and_entry(root, "No. de Cotizacion", "white", "black", 35, 45, 230, 15, 260) #<- cambiar a un metodo automatizado
    # Numero de Servicio
    create_label_and_entry(root, "Numero de Servicio", "white", "black", 35, 330, 230, 300, 260)

    # Tarifa
    # text_label7 = tk.Label(root, text="Tarifa", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    # text_label7.place(x=45, y=330)  # Set the position of the label
    # options = ["01", "PBDT", "DAC", "GDMTO"]
    # selected_option = tk.StringVar(root)
    # selected_option.set(options[0])  # Set the default selected option
    # option_menu = tk.OptionMenu(root, selected_option, *options, command=on_option_selected)
    # option_menu.config(width=15, anchor="center", bg="white", fg="black")  # Set background and text color of the menu
    # option_menu["menu"].config(bg="white", fg="black")  # Set background and text color of the dropdown menu
    # option_menu.place(x=45, y=370, width=200)

    # Create the input box (Numero De Servicio)
    # text_label5 = tk.Label(root, text="No. de Servicio", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    # text_label5.place(x=335, y=200)  # Set the position of the label
    # entry4 = tk.Entry(root,bg="white",highlightthickness=0, relief=tk.FLAT,fg="black",width=30)
    # entry4.place(x=300, y=230)

    # Create a button to open the pop-up window
    promedio_button = tk.Button(root, text="Edit Promedio", command=open_promedio_bimestral_window)
    promedio_button.place(x=225, y=370)

    # Create a button to read the input and print it
    button = tk.Button(root, bg="#D3D3D3", fg="black", text="Submit", command=on_button_click, font=("Arial", 12, "bold"))
    button.place(x=550, y=500,width=100, height=40)


    root.mainloop()
