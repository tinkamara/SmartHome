class TxtWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_text(self, text):
        try:
            with open(self.file_path, 'w') as file:
                file.write(text)
            print("Die Daten wurden erfolgreich in die Textdatei geschrieben.")
        except IOError:
            print("Beim Schreiben der Daten ist ein Fehler aufgetreten.")