import subprocess
import winreg
import sys
from colorama import Fore, init

# Initialisation de colorama
init(autoreset=True)


def get_installed_software():
    """
    Récupère les logiciels installés via le registre Windows
    """
    software_list = []
    reg_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]
    
    for reg_path in reg_paths:
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
        except FileNotFoundError:
            continue

        for i in range(0, winreg.QueryInfoKey(key)[0]):
            try:
                subkey_name = winreg.EnumKey(key, i)
                subkey = winreg.OpenKey(key, subkey_name)
                try:
                    name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                except FileNotFoundError:
                    continue
                try:
                    version = winreg.QueryValueEx(subkey, "DisplayVersion")[0]
                except FileNotFoundError:
                    version = "Inconnue"
                software_list.append((name, version))
            except OSError:
                continue
    return software_list


def get_winget_updates():
    """
    Récupère la liste des logiciels que Winget peut mettre à jour
    """
    try:
        result = subprocess.run(
            ["winget", "upgrade"],
            capture_output=True, text=True
        )
        updates = result.stdout.strip().splitlines()
        return updates[2:]  # enlève l'en-tête
    except FileNotFoundError:
        print(Fore.RED + "! Winget n'est pas disponible sur ce système !")
        return []


def show_progress(index, total):
    """
    Affiche une barre de progression en blanc
    """
    progress = int((index / total) * 30)
    bar = "■" * progress + "-" * (30 - progress)
    percent = int((index / total) * 100)
    sys.stdout.write(Fore.WHITE + f"\r[{bar}] {percent}%")
    sys.stdout.flush()


def verify_update(software_name):
    """
    Vérifie la version installée après une mise à jour
    """
    installed = get_installed_software()
    for name, version in installed:
        if software_name.lower() in name.lower():
            return version
    return None


def print_commands():
    """
    Affiche la liste des commandes disponibles
    """
    print(Fore.LIGHTRED_EX + "\nCommandes disponibles :")
    print("  list           → Afficher les logiciels installés")
    print("  updates        → Vérifier les mises à jour disponibles (via Winget)")
    print("  upgrade all    → Mettre à jour tous les logiciels")
    print("  upgrade <ID>   → Mettre à jour un logiciel spécifique (ID Winget)")
    print("  exit           → Quitter\n")


def command_loop():
    """
    Boucle principale interactive
    """
    print(Fore.LIGHTRED_EX + "\n=== Gestionnaire de mises à jour (Python + Winget) ===")
    print_commands()

    while True:
        cmd = input(Fore.LIGHTRED_EX + "> ").strip()

        if cmd == "list":
            installed = get_installed_software()
            total = len(installed)
            print(Fore.LIGHTRED_EX + f"\nLogiciels installés ({total}):\n")
            for index, (name, version) in enumerate(installed, start=1):
                show_progress(index, total)
            print("\n")
            for name, version in installed:
                print(Fore.WHITE + f"{name} — {version}")
            print_commands()

        elif cmd == "updates":
            print(Fore.LIGHTRED_EX + "\nVérification des mises à jour...\n")
            updates = get_winget_updates()
            if not updates:
                print(Fore.LIGHTRED_EX + "Tous les logiciels sont à jour (selon Winget).")
            else:
                print(Fore.LIGHTRED_EX + "Logiciels avec mises à jour disponibles :\n")
                for line in updates:
                    print(line)
            print_commands()

        elif cmd == "upgrade all":
            print(Fore.LIGHTRED_EX + "\nMise à jour de tous les logiciels disponibles...\n")
            subprocess.run(["winget", "upgrade", "--all"])
            print(Fore.GREEN + "Mise à jour terminée.")
            print_commands()

        elif cmd.startswith("upgrade "):
            software_id = cmd.split(" ", 1)[1]
            print(Fore.LIGHTRED_EX + f"\nMise à jour de {software_id}...\n")
            subprocess.run(["winget", "upgrade", "--id", software_id])

        elif cmd == "exit":
            print(Fore.LIGHTRED_EX + "Au revoir !")
            break

        else:
            print(Fore.RED + "Commande inconnue.")
            print_commands()


if __name__ == "__main__":
    command_loop()
