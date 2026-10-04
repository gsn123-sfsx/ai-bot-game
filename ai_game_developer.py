import os
import subprocess
import time

class AIGameDeveloperBot:
    def __init__(self, project_name="generated_game"):
        self.project_name = project_name
        self.code_file = f"{project_name}.py"
        self.version = 1

    def generate_initial_code(self):
        """Generuje pierwszą, prostą wersję gry (np. bazę pod grę zręcznościową)."""
        print(f"[*] Tworzenie wersji v{self.version} bazy gry...")
        
        # Kod prostej gry w Pygame lub konsolowej (tutaj wersja konsolowa/Pygame do rozbudowy)
        code = """# Wersja v1 bota gry
import random
import time

def run_game():
    print("--- START GRY: ZBIERAJ PUNKTY ---")
    score = 0
    for step in range(5):
        action = random.choice(["skok", "atak", "bieg"])
        print(f"Krok {step+1}: Wykonano akcję -> {action}")
        score += 10
        time.sleep(0.2)
    print(f"Koniec gry! Twój wynik: {score}")

if __name__ == "__main__":
    run_game()
"""
        with open(self.code_file, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"[+] Zapisano kod do pliku {self.code_file}")

    def test_and_debug_code(self):
        """Uruchamia wygenerowany kod i sprawdza, czy nie ma w nim błędów (samonaprawa)."""
        print(f"[*] Testowanie kodu wdrożeniowego v{self.version}...")
        
        # Uruchamiamy napisany kod jako oddzielny proces
        result = subprocess.run(["python", self.code_file], capture_output=True, text=True)
        
        if result.returncode != 0:
            print("[-] Wykryto błąd w kodzie!")
            print(result.stderr)
            # Tutaj bot mógłby wysłać błąd do modelu AI z prośbą o korektę
            return False
        else:
            print("[+] Kod działa bezbłędnie!")
            print(result.stdout)
            return True

    def evolve_game(self):
        """Rozwija grę – dodaje nowe funkcje, zmieniając kod na bardziej zaawansowany."""
        self.version += 1
        print(f"\n[*] Ewolucja bota: Przechodzenie do wersji v{self.version} (dodawanie nowych mechanik)...")
        
        # Bardziej rozbudowany kod z kolejnej iteracji
        advanced_code = f"""# Wersja v{self.version} bota gry - rozbudowana o trudność i poziomy
import random
import time

def run_game():
    print("--- START GRY v{self.version}: TRYB ZAAWANSOWANY ---")
    score = 0
    level = 1
    for step in range(8):
        action = random.choice(["skok", "unik", "atak specjalny", "obrona"])
        print(f"Poziom {level} | Krok {step+1}: Akcja -> {{action}}")
        score += 25
        if step == 4:
            level += 1
            print(f">> AWANS NA POZIOM {level}! <<")
        time.sleep(0.1)
    print(f"Koniec gry v{self.version}! Ostateczny wynik: {{score}}")

if __name__ == "__main__":
    run_game()
"""
        with open(self.code_file, "w", encoding="utf-8") as f:
            f.write(advanced_code)
        print(f"[+] Zaktualizowano kod do wersji v{self.version}")

# --- URUCHOMIENIE BOTA ---
if __name__ == "__main__":
    bot = AIGameDeveloperBot()
    
    # Krok 1: Stworzenie bazy
    bot.generate_initial_code()
    bot.test_and_debug_code()
    
    time.sleep(1)
    
    # Krok 2: Ewolucja i tworzenie lepszej wersji gry
    bot.evolve_game()
    bot.test_and_debug_code()
