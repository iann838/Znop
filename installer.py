import os

installer = 'pyinstaller --noconfirm --onefile --console --icon "C:/Users/Spanish/Desktop/Znop/favicon.ico" --name "Znop" --add-data "C:/Users/Spanish/Desktop/Znop/znop;znop/" --add-data "C:/Users/Spanish/Desktop/Znop/LICENSE;." --add-data "C:/Users/Spanish/Desktop/Znop/README.md;."  "C:/Users/Spanish/Desktop/Znop/__main__.py"'

if __name__ == "__main__":
    os.system(installer)
