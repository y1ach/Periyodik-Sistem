import json

# JSON dosyasını oku
with open(r"C:\Users\yigit\OneDrive\Desktop\Yazılım\Periyodik Sistem\elements.json", "r", encoding="utf-8") as f:
    elements = json.load(f)

# Kullanıcıdan girdi al
periyot = int(input("Periyot gir: "))
grup = int(input("Grup gir: "))

# JSON içinde ara
found = None
for elmt in elements:
    if elmt["Satır"] == periyot and elmt["Sütun"] == grup:
        found = elmt
        break

# Sonucu göster
if found:
    print(f"Element: {found['isim']} ({found['Sembol']}) \r")
    print("\r")
    print(f"Bilgi: {found['İnfo']}")
else:
    print("Böyle bir element yok.")
