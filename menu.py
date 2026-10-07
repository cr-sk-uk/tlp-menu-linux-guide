#!/usr/bin/env python3
import subprocess
import sys

def run(cmd, need_sudo=True):
    """Запустить команду, вернуть вывод."""
    full = (["sudo", "-n"] if need_sudo else []) + cmd
    try:
        r = subprocess.run(full, capture_output=True, text=True, check=True)
        return r.stdout or "OK"
    except subprocess.CalledProcessError as e:
        return f"Ошибка: {e.stderr.strip()}"

def tlp(action):
    print(f">>> tlp {action}")
    print(run(["tlp", action]))

def show_status():
    print(">>> tlp-stat (кратко)")
    print(run(["tlp-stat", "-s"]))

def show_battery():
    print(">>> tlp-stat -b (батарея)")
    print(run(["tlp-stat", "-b"]))

def show_config():
    print(">>> tlp-stat -c (конфиг)")
    print(run(["tlp-stat", "-c"]))

def open_gui():
    print(">>> Запускаю TLPUI...")
    subprocess.Popen(["flatpak", "run", "com.github.d4nj1.tlpui"])

def menu():
    while True:
        print("""
╔══════════════════════════════╗
║        TLP МЕНЮ              ║
╠══════════════════════════════╣
║ 1. Включить TLP (start)      ║
║ 2. Режим батареи (bat)       ║
║ 3. Режим сети (ac)           ║
║ 4. USB-авто (usb)            ║
║ 5. Зарядить один раз         ║
║ 6. Полный заряд (100%)       ║
║ 7. Разрядить батарею         ║
║ 8. Статус (кратко)           ║
║ 9. Инфо о батарее            ║
║ 10. Показать конфиг          ║
║ 11. Открыть TLPUI (GUI)      ║
║ 0. Выход                     ║
╚══════════════════════════════╝
""")
        c = input("Выбор: ").strip()

        if   c == "1":  tlp("start")
        elif c == "2":  tlp("bat")
        elif c == "3":  tlp("ac")
        elif c == "4":  tlp("usb")
        elif c == "5":  tlp("chargeonce")
        elif c == "6":  tlp("fullcharge")
        elif c == "7":  tlp("discharge")
        elif c == "8":  show_status()
        elif c == "9":  show_battery()
        elif c == "10": show_config()
        elif c == "11": open_gui()
        elif c == "0":
            print("Пока, кент! 👋")
            sys.exit(0)
        else:
            print("Нет такого пункта, попробуй снова.")

if __name__ == "__main__":
    menu()
