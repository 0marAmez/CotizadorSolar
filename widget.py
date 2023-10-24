import tkinter as tk
import openpyxl
import math
import locale
from PIL import Image, ImageTk
from datetime import date
from openpyxl.styles import Font
from  solar import PanelSolar
from graph import create_bar_graph
from openpyxl.drawing.image import Image as xlImage

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

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

def on_button_click_pop_window():
    
    valores_bimestrales = []
    periodo_bimestrales = []
    # Guarda los valores del menu de promedios
    valores_bimestrales.append(float(entry_widgets["Bimestre I"].get()))
    periodo_bimestrales. append(entry_widgets["Periodo del Bimestre I"].get())
    valores_bimestrales.append(float(entry_widgets["Bimestre II"].get()))
    periodo_bimestrales. append(entry_widgets["Periodo del Bimestre II"].get())
    valores_bimestrales.append(float(entry_widgets["Bimestre III"].get()))
    periodo_bimestrales. append(entry_widgets["Periodo del Bimestre III"].get())
    valores_bimestrales.append(float(entry_widgets["Bimestre IV"].get()))
    periodo_bimestrales. append(entry_widgets["Periodo del Bimestre IV"].get())
    valores_bimestrales.append(float(entry_widgets["Bimestre V"].get()))
    periodo_bimestrales. append(entry_widgets["Periodo del Bimestre V"].get())
    valores_bimestrales.append(float(entry_widgets["Bimestre VI"].get()))
    periodo_bimestrales. append(entry_widgets["Periodo del Bimestre VI"].get())


    # Calcula el promedio
    total = sum(valores_bimestrales)
    average = total / len(valores_bimestrales)
    entry_widgets["Promedio"] = str(average)


    produccion_del_sistema = (average/0.5)
    produccion_del_sistema = (produccion_del_sistema /0.6)
    produccion_del_sistema = (produccion_del_sistema /550) # cantidad de paneles
    produccion_del_sistema = math.ceil(produccion_del_sistema) # ajustar al entero mas cercano
    produccion_del_sistema = produccion_del_sistema*550 
    produccion_del_sistema = (produccion_del_sistema/1000)*5*60 # produccion_del_sistema

    solar_energy_bimestre = [produccion_del_sistema for _ in range(6)]

    # Crea grafo
    create_bar_graph(solar_energy_bimestre,valores_bimestrales,periodo_bimestrales)


def open_promedio_bimestral_window():
    # Create a new window
    promedio_window = tk.Toplevel(root)
    # Set the width and height as needed
    promedio_window.geometry("600x700")
    promedio_window.configure(bg="#FCD12A")  # Set your desired background color  

    # Bimestre I
    create_label_and_entry(promedio_window, "Bimestre I", "white", "black", 30, 65, 15, 15, 50)
    create_label_and_entry(promedio_window, "Periodo del Bimestre I", "white", "black", 30, 305, 15, 305, 50)
    # Bimestre II
    create_label_and_entry(promedio_window, "Bimestre II", "white", "black", 30, 65, 115, 15, 150)
    create_label_and_entry(promedio_window, "Periodo del Bimestre II", "white", "black", 30, 305, 115, 305, 150)
    # Bimestre III
    create_label_and_entry(promedio_window, "Bimestre III", "white", "black", 30, 65, 215, 15, 250)
    create_label_and_entry(promedio_window, "Periodo del Bimestre III", "white", "black", 30, 305, 215, 305, 250)
    # Bimestre IV
    create_label_and_entry(promedio_window, "Bimestre IV", "white", "black", 30, 65, 315, 15, 350)
    create_label_and_entry(promedio_window, "Periodo del Bimestre IV", "white", "black", 30, 305, 315, 305, 350)
    # # Bimestre V
    create_label_and_entry(promedio_window, "Bimestre V", "white", "black", 30, 65, 415, 15, 450)
    create_label_and_entry(promedio_window, "Periodo del Bimestre V", "white", "black", 30, 305, 415, 305, 450)
    # # Bimestre VI
    create_label_and_entry(promedio_window, "Bimestre VI", "white", "black", 30, 65, 515, 15, 550)
    create_label_and_entry(promedio_window, "Periodo del Bimestre VI", "white", "black", 30, 305, 515, 305, 550)

    # Create a button to close the new window
    close_button = tk.Button(promedio_window, text="Guardar", command=on_button_click_pop_window)
    close_button.place(x=450, y=600)

def on_button_click():
    # Saca los valores del widget
    cliente = entry_widgets["Nombre del recibo"].get()
    direccion = entry_widgets["Direccion"].get()
    no_cotizacion = entry_widgets["No. de Cotizacion"].get()
    no_servicio = entry_widgets["Numero de Servicio"].get()
    vendedor = entry_widgets["Vendedor"].get()
    tarifa = entry_widgets["Tarifa"]
    promedio = round(float((entry_widgets["Promedio"])))


    workbook = openpyxl.load_workbook("template/SolarEnergyTemplate.xlsx")
    worksheet = workbook.active

    paneles =  PanelSolar(promedio)
    paneles.calcular_paneles()
    paneles.info_inversor()

    nombre_completo = cliente.split()
    worksheet['F9'] = 'Aguascalientes, Ags  '+ str(date.today())
    worksheet['C12'] = cliente
    worksheet['C13'] = direccion
    worksheet['I12'] = no_cotizacion
    worksheet['I13'] = no_servicio
    worksheet['H14'] = tarifa


    worksheet['D22'] = str(round(promedio)) + " kwh/bimestrales"
    worksheet['D23'] = str(paneles.capacidad_instalar)+" kwp"
    worksheet['D24'] = str(round(paneles.produccion_del_sistema))+" kwh/bm"

    # Paneles
    worksheet['F28'] = paneles.cantidad_de_paneles
    worksheet['G28'] = locale.currency(paneles.costo_de_paneles, grouping=True)
    # Inversor
    worksheet['C31'] = "Inversor GROWATT "+paneles.modelo_inversor
    worksheet['F31'] = paneles.cantidad_inversores
    worksheet['G31'] = locale.currency(paneles.costo_invesor, grouping=True)
    # Mano de Obra
    worksheet['G34'] = locale.currency(paneles.costo_de_obra, grouping=True)
    # Total
    worksheet['G45'] = locale.currency(paneles.costo_de_obra+paneles.costo_de_paneles+paneles.costo_invesor, grouping=True)

    # Vendedor
    worksheet['B47'] = "Lic. "+vendedor

    # Save the image to a file (replace 'your_image.png' with the actual image file)
    image_file = 'plot.png'

    # Insert the image into cell B54
    image_file = 'plot.png'

    # Insert the image into cell B54
    img = xlImage(image_file)
    worksheet.add_image(img, 'B54')


    bold_font = Font(bold=True)
    worksheet['D22'].font = bold_font
    worksheet['D23'].font = bold_font
    worksheet['D24'].font = bold_font
    worksheet['B47'].font = bold_font


    new_file_name = f"{nombre_completo[0]+'_'+nombre_completo[2]+str(date.today())}_cotizacion.xlsx"
    cotizacion = 'cotizaciones/' +new_file_name

    workbook.save(cotizacion)
    workbook.close()


def on_option_selected(selected_option):
    # print("Selected Option:", selected_option)
    entry_widgets["Tarifa"] = selected_option
    

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

    # Tarifa (Opciones)
    text_label_tarifa = tk.Label(root, text="Tarifa", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label_tarifa.place(x=85, y=330)  # Set the position of the label
    options = ["01", "PBDT", "DAC", "GDMTO"]
    selected_option = tk.StringVar(root)
    selected_option.set(options[0])  # Set the default selected option
    option_menu = tk.OptionMenu(root, selected_option, *options, command=on_option_selected)
    option_menu.config(width=15, anchor="center", bg="white", fg="black")  # Set background and text color of the menu
    option_menu["menu"].config(bg="white", fg="black")  # Set background and text color of the dropdown menu
    option_menu.place(x=15, y=360, width=200)

    # Create a button to open the pop-up window for the Promedio the kwh
    text_label_Promedio = tk.Label(root, text="Promedio", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label_Promedio.place(x=370, y=330)  # Set the position of the label
    promedio_button = tk.Button(root, text="Editar Promedio", command=open_promedio_bimestral_window)
    promedio_button.place(x=305, y=360, width=210, height=30)

    # Vendedor
    create_label_and_entry(root, "Vendedor", "white", "black", 35, 220, 430, 160, 460)

    # Create a button to read the input and print it
    button = tk.Button(root, bg="#D3D3D3", fg="black", text="Submit", command=on_button_click, font=("Arial", 12, "bold"))
    button.place(x=550, y=500,width=100, height=40)


    root.mainloop()
