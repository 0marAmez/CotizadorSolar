import tkinter as tk
import openpyxl
from PIL import Image, ImageTk
from datetime import date
from openpyxl.styles import Font



inversor = {2000:330 , 
        2500: 360, 
        3000: 400,
        3300: 420,
        3600:503,
        4200:520,
        4600:539,
        5000:570,
        6000:610,
        7000:860,
        8000:880,
        9000:1000,
        10000:1020,
        }
def calcular_paneles(kw_bimestral):
    total_paneles = 0

    total_paneles = (kw_bimestral/0.5)

    total_paneles = (total_paneles /0.6)

    total_paneles = total_paneles/550

    total_paneles = round(total_paneles)

    costo_paneles = total_paneles*145*20 # costo por panel solar

    costo_paneles += (50*20)  # Complementos, siempre 1 gabinete?

    costo_paneles += (650*total_paneles) # aceros alcalde

    costo_paneles += (1000*total_paneles) # mano de obra

    costo_paneles += 1000+1000+500+1500 #Gastos de mano de obra, Cable, Tornillos,Complementos

    return total_paneles,costo_paneles

def calcular_inversor(total_paneles):

    capacidad_instalar = total_paneles*550

    # print(capacidad_instalar)

    modelo_invesor =  min(inversor, key=lambda x: abs(x - capacidad_instalar))

    # print(modelo_invesor)

    costo_invesor = inversor[modelo_invesor]*20

    return (capacidad_instalar/1000),modelo_invesor,costo_invesor

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
    numero_de_servicio = entry2.get()
    direccion = entry3.get()
    vendedor = entry4.get()
    promedio_kw =entry6.get()

    workbook = openpyxl.load_workbook("template/SolarEnergyTemplate.xlsx")
    worksheet = workbook.active

    paneles_info =  calcular_paneles(float(promedio_kw))
    inversor_info = calcular_inversor(paneles_info[0])

    primernombre = cliente.split()
    worksheet['B11'] = cliente
    worksheet['E3'] = 'Aguascalientes, Ags  '+ str(date.today())
    worksheet['E6'] = vendedor
    worksheet['B13'] = direccion
    # worksheet['G11'] = date.strftime("%b")[0]+"1234"
    worksheet['G11'] = "Testeo"
    worksheet['G12'] = str(numero_de_servicio)
    worksheet['G13'] = "test"
    worksheet['C21'] = inversor_info[0]
    worksheet['C22'] = str(promedio_kw) + ' kwh/bimestral'

    worksheet['A25'] = "1"
    worksheet['A26'] = "2"
    worksheet['A27'] = "3"

    worksheet ['C25'] = "PANEL SOLAR LONGI 550W monocristalino 144 celulas (6x24)"
    worksheet ['C26'] = "INVERSOR GROWATT "+str(inversor_info[1])+" TLX"
    worksheet ['C27'] = "Fabricación y montaje de estructura para 7 módulos, incluye ingeniería, mano de obra, cableado, ductería, tornillería, adoquines, gabinetes y protecciones, puesta en marca de acuerdo a la NOM-001-SEDE-2012 y tramites ante CFE."

    worksheet['F25'] = str(paneles_info[0])
    worksheet['F26'] = "1"
    worksheet['F27'] = "1"

    worksheet['H25'] = str(paneles_info[1])
    worksheet['H26'] = str(inversor_info[2])
    worksheet['H27'] = "1"



    bold_font = Font(bold=True)
    worksheet['B11'].font = bold_font
    worksheet['B13'].font = bold_font
    worksheet['G11'].font = bold_font
    worksheet['G12'].font = bold_font
    worksheet['G13'].font = bold_font

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
    text_label1.place(x=550, y=80)  # Set the position of the label




    # Image Label
    image_path = "solar.jpg"
    width, height = 200, 100
    tk_image = load_and_resize_image(image_path, width, height)
    # Create a label to display the image
    label = tk.Label(root, image=tk_image, bg="white")
    label.place(x=0 ,y=0)  # Set the label's coordinates



    # Create the input box (Nombre del recibo)
    text_label1 = tk.Label(root, text="Nombre del recibo", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label1.place(x=75, y=180)  # Set the position of the label
    entry1 = tk.Entry(root,bg="white",highlightthickness=0, relief=tk.FLAT,fg="black")
    entry1.place(x=40, y=200)


    # Create the input box (Numero de Servicio)
    text_label2 = tk.Label(root, text="Numero de Servicio", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label2.place(x=335, y=180)  # Set the position of the label
    entry2 = tk.Entry(root,bg="white",highlightthickness=0, relief=tk.FLAT,fg="black")
    entry2.place(x=300, y=200)


    # Create the input box (Direccion)
    text_label3 = tk.Label(root, text="Direccion", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label3.place(x=100, y=280)  # Set the position of the label
    entry3 = tk.Entry(root,bg="white",highlightthickness=0, relief=tk.FLAT,fg="black")
    entry3.place(x=40, y=300)


    # Create the input box (Vendedor)
    text_label4 = tk.Label(root, text="Vendedor", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label4.place(x=360, y=280)  # Set the position of the label
    entry4 = tk.Entry(root,bg="white",highlightthickness=0, relief=tk.FLAT,fg="black")
    entry4.place(x=300, y=300)


    # Create the input box (Opciones)
    text_label5 = tk.Label(root, text="Seleccione una Opcion", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label5.place(x=65, y=380)  # Set the position of the label
    options = ["01", "PBDT", "DAC", "GDMTO"]
    selected_option = tk.StringVar(root)
    selected_option.set(options[0])  # Set the default selected option
    option_menu = tk.OptionMenu(root, selected_option, *options, command=on_option_selected)
    option_menu.config(width=15,anchor="center")  # Set a fixed width of 15 characters for the menu
    option_menu.configure(bg=root.cget("bg"))  # Set the background color of the menu to be white
    option_menu["menu"].configure(bg="white")  # Set the background color of the dropdown menu
    option_menu["menu"].configure(fg="black")  # Set the color of the letters (text) in the drop-down menu to blue
    option_menu.place(x=40, y=400)


    # Create the input box (Opciones)
    text_label6 = tk.Label(root, text="Promedio Bimestral", bg="#FCD12A", font=("Arial", 12, "bold"), fg="black")
    text_label6.place(x=335, y=380)  # Set the position of the label
    entry6 = tk.Entry(root,bg="white",highlightthickness=0, relief=tk.FLAT,fg="black")
    entry6.place(x=300, y=400)



    # Create a button to read the input and print it
    button = tk.Button(root, bg="white", text="Submit", command=on_button_click, relief=tk.FLAT, highlightthickness=0, highlightbackground="#FCD12A")
    button.place(x=550, y=500)


    root.mainloop()
