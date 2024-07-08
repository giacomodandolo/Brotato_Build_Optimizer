import PySimpleGUI as sg
from Weapons import weapon_scrape as ws

# Create GUI
def createWindow():
    sg.theme("DarkBrown2")
    confLayout = [[sg.Text("This is an app designed to scrape Brotato Weapons.", key = "intro")],
                  [sg.Text(" ", key = "updated", text_color = "green")],
                  [sg.Button("Obtain Weapons"), sg.Button("To CSV", visible = False), sg.Button("To MD", visible = False)],
                 ]
    window = sg.Window(title = "Brotato Weapon Scraping", layout = confLayout)

    while True:
        event, values = window.read()
        
        if event == "Obtain Weapons":
            ws.obtainWeapons()
            window["To CSV"].update(visible = True)
            window["To MD"].update(visible = True)
            window["updated"].update("Weapons obtained!")
        
        if event == "To CSV":
            ws.obtainCSV()
            window["updated"].update("CSV updated!")

        if event == "To MD":
            ws.obtainMD()
            window["updated"].update("MD updated!")

        if event == sg.WIN_CLOSED:
            break

    window.close()

createWindow()