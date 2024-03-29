import os
import yt_dlp
import customtkinter as ctk
from tkinter.filedialog import askdirectory

global title
title = "%(title)s - %(uploader)s"


class titleToplevel(ctk.CTkToplevel):
    def __init__(self, entry):
        super().__init__()
        global title
        self.title("Titolo Avanzato")
        self.geometry("500x140")
        self.resizable(False, False)

        defaultTitle = "%(title)s - %(uploader)s"
        self.titleEntry = ctk.CTkEntry(self, width=480, height=28, font=("Noto Sans", 13))
        self.titleEntry.insert("end", title)
        self.titleEntry.place(x=10, y=5)

        tags = ["Titolo", "ID", "Descrizione", "Nome Creatore", "ID Creatore", "URL Creatore", "Data Caricamento (YYYYMMDD)", "Data Pubblicazione (YYYYMMDD)", "Anno Pubblicazione (YYYY)", "Nome Canale", "ID Canale", "URL Canale", "Iscritti Canale", "Canale Verificato (True, False)", "Durata (HH:mm:ss)", "Durata (secondi)", "Visualizzazioni", "Like", "Dislike"]
        self.tagDropdown = ctk.CTkOptionMenu(self, values=tags, font=("Noto Sans", 13), dynamic_resizing=False)
        self.tagDropdown.place(x=10, y=50)

        self.tagButton = ctk.CTkButton(self, corner_radius=64, text="Aggiungi Tag", font=("Noto Sans", 14))
        def addTag():
            selectedTag = self.tagDropdown.get()
            match selectedTag:
                case "Titolo":
                    self.titleEntry.insert("end", "%(title)s")
                case "ID":
                    self.titleEntry.insert("end", "%(id)s")
                case "Descrizione":
                    self.titleEntry.insert("end", "%(description)s")
                case "Nome Creatore":
                    self.titleEntry.insert("end", "%(uploader)s")
                case "ID Creatore":
                    self.titleEntry.insert("end", "%(uploader_id)s")
                case "URL Creatore":
                    self.titleEntry.insert("end", "%(uploader_url)s")
                case "Data Caricamento (YYYYMMDD)":
                    self.titleEntry.insert("end", "%(upload_date)s")
                case "Data Pubblicazione (YYYYMMDD)":
                    self.titleEntry.insert("end", "%(release_date)s")
                case "Anno Pubblicazione (YYYY)":
                    self.titleEntry.insert("end", "%(release_year)s")
                case "Nome Canale":
                    self.titleEntry.insert("end", "%(channel)s")
                case "ID Canale":
                    self.titleEntry.insert("end", "%(channel_id)s")
                case "URL Canale":
                    self.titleEntry.insert("end", "%(channel_url)s")
                case "Iscritti Canale":
                    self.titleEntry.insert("end", "%(channel_follower_count)s")
                case "Canale Verificato (True, False)":
                    self.titleEntry.insert("end", "%(channel_is_verified)s")
                case "Durata (HH:mm:ss)":
                    self.titleEntry.insert("end", "%(duration)s")
                case "Durata (secondi)":
                    self.titleEntry.insert("end", "%(duration_string)s")
                case "Visualizzazioni":
                    self.titleEntry.insert("end", "%(view_count)s")
                case "Like":
                    self.titleEntry.insert("end", "%(like_count)s")
                case "Dislike":
                    self.titleEntry.insert("end", "%(dislike_count)s")

        self.tagButton.configure(command=addTag)
        self.tagButton.place(x=160, y=50)

        def setDefault():
            self.titleEntry.delete(0, "end")
            self.titleEntry.insert("end", defaultTitle)
        self.defaultButton = ctk.CTkButton(self, corner_radius=64, text="Default", font=("Noto Sans", 14), command=setDefault)
        self.defaultButton.place(x=490, y=50, anchor="ne")

        def ok():
            global title
            newTitle = self.titleEntry.get()
            title = self.titleEntry.get()
            entry.delete(0, "end")
            entry.insert("end", newTitle)
            print(newTitle)
            self.destroy()
        self.okButton = ctk.CTkButton(self, corner_radius=64, text="Ok", font=("Noto Sans", 14), command=ok)
        self.okButton.place(x=250, y=110, anchor="center")


class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Video Downloader")
        self.geometry("900x675")
        self.resizable(False, False)

        

        self.urlInput = ctk.CTkEntry(self, width=500, height=30, corner_radius=64, font=("Noto Sans", 13), placeholder_text="URL")
        self.urlInput.place(x=115, y=168.75, anchor="w")

        self.urlButton = ctk.CTkButton(self, text="Verifica URL", font=("Noto Sans", 14), corner_radius=60)
        self.urlButton.place(x=785, y=168.75, anchor="e")

        self.infoFrame = ctk.CTkFrame(self, width=810, height=400, corner_radius=64)
        self.infoFrame.place(x=450, y=420, anchor="center")

        self.titleInput = ctk.CTkEntry(self.infoFrame, width=420, height=28, corner_radius=54, font=("Noto Sans", 13), placeholder_text="Titolo")
        self.titleInput.place(x=110, y=75, anchor="w")

        self.advancedTitleButton = ctk.CTkButton(self.infoFrame, corner_radius=60, text="Titolo Avanzato", font=("Noto Sans", 13))
        def fileName():
            titleToplevel(entry=self.titleInput)
        self.advancedTitleButton.configure(command=fileName)
        self.advancedTitleButton.place(x=700, y=75, anchor="e")

        self.pathInput = ctk.CTkEntry(self.infoFrame, width=420, height=28, corner_radius=54, font=("Noto Sans", 13), placeholder_text="Percorso")
        self.pathInput.place(x=110, y=175, anchor="w")
        print(self.pathInput.cget("width"))

        def askdirectoryfunc():
            path = askdirectory()
            self.pathInput.delete(0, "end")
            self.pathInput.insert("end", path)
        self.pathButton = ctk.CTkButton(self.infoFrame, corner_radius=60, text="Cambia Percorso", font=("Noto Sans", 13), command=askdirectoryfunc)
        self.pathButton.place(x=700, y=175, anchor="e")
        print(self.pathButton.cget("width"))

        self.extensionLabel = ctk.CTkLabel(self.infoFrame, text="Formato", font=("Noto Sans", 13))
        self.extensionLabel.place(x=230, y=245, anchor="center")

        self.extensionDropdown = ctk.CTkOptionMenu(self.infoFrame, values=["N/A"], font=("Noto Sans", 13))
        self.extensionDropdown.place(x=230, y=275, anchor="center")

        self.resolutionLabel = ctk.CTkLabel(self.infoFrame, text="Risoluzione", font=("Noto Sans", 13))
        self.resolutionLabel.place(x=580, y=245, anchor="center")

        self.resolutionDropdown = ctk.CTkOptionMenu(self.infoFrame, values=["N/A"], font=("Noto Sans", 13))
        self.resolutionDropdown.place(x=580, y=275, anchor="center")

        def main_video_ops():
            video_url = self.urlInput.get()
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=False)
                formats = info_dict.get('formats', [])
                extensions = []
                ext_resolutions = {}
                for format in formats:
                    ext = format['ext']
                    if ext not in extensions:
                        extensions.append(ext)
                    resolution = format.get('format_note', 'Unknown')
                    if ext != "Unknown" and ext not in ext_resolutions:
                        ext_resolutions[ext] = []
                    if resolution != "Unknown" and resolution not in ext_resolutions[ext]:
                        print(resolution)
                        ext_resolutions[ext].append(resolution)
                
                extensions.append("Audio")
                ext_resolutions["Audio"] = []
                ext_resolutions["Audio"].append("Migliore")
                self.extensionDropdown.configure(values=extensions)

                # Corrected lambda function to pass the selected extension to update_resolutions
                self.extensionDropdown.configure(command=lambda _: update_resolutions(ext_resolutions, self.extensionDropdown.get()))

        def update_resolutions(ext_resolutions, selected_ext):
            if selected_ext in ext_resolutions:
                resolutions = ext_resolutions[selected_ext]
                self.resolutionDropdown.configure(values=resolutions)
            else:
                self.resolutionDropdown.configure(values=["N/A"])

                
        self.urlButton.configure(command=main_video_ops)

        self.downloadButton = ctk.CTkButton(self.infoFrame, corner_radius=50, text="Scarica", font=("Noto Sans", 20), width=150, height=75)
        self.downloadButton.place(x=405, y=350, anchor="center")
        def download_video():
            video_url = self.urlInput.get()
            selected_ext = self.extensionDropdown.get()
            selected_res = self.resolutionDropdown.get()

            download_dir = self.pathInput.get()

            print(self.pathInput.get())

            if selected_ext == "Audio" and selected_res == "Migliore":
                format_code = 'bestaudio/best'
            else:
                format_code = f"{selected_ext}/{selected_res}"

            ydl_opts = {
                'quiet': False,
                'no_warnings': False,
                'format': format_code,
                'outtmpl': download_dir + "/" + title + ".%(ext)s",
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
        self.downloadButton.configure(command=download_video)


app = Main()
app.mainloop()