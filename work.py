from pynput.mouse import Button, Controller
import time

mouse_controller = Controller()

# --- CONFIGURATION ---
# Yahan apne note kiye hue coordinates (X, Y) format mein daalein
coordinates_to_click = [
    (95, 87),    # Pehla coordinate (X=95, Y=87)
    (653, 726)   # Dusra coordinate (X=653, Y=726)
    # Agar aur coordinates hain, toh yahan (X, Y) format mein add karein
]

DELAY_BETWEEN_CLICKS_SECONDS = 10  # Har click ke beech ka samay (seconds mein)
DELAY_BETWEEN_LOOPS_HOURS = 1      # Har loop ke baad kitne ghante intezar karna hai
# --- END CONFIGURATION ---

delay_between_loops_seconds = DELAY_BETWEEN_LOOPS_HOURS * 3600 # Ghante ko seconds mein convert karein

def perform_click_sequence():
    if not coordinates_to_click:
        print("Koi coordinates nahi diye gaye. Script band ho rahi hai.")
        return False # Indicate that no clicks were performed

    print(f"Click sequence shuru ho raha hai...")
    for i, (x, y) in enumerate(coordinates_to_click):
        print(f"Coordinate {i+1}/{len(coordinates_to_click)}: ({x}, {y}) par jaa raha hai...")
        mouse_controller.position = (x, y)
        time.sleep(0.2) # Mouse ko settle hone ke liye thoda waqt dein
        
        mouse_controller.click(Button.left, 1) # Left click
        print(f"({x}, {y}) par click kiya.")
        
        # Agar yeh sequence ka aakhri click nahi hai, toh 10 second wait karein
        if i < len(coordinates_to_click) - 1:
            print(f"{DELAY_BETWEEN_CLICKS_SECONDS} seconds intezar...")
            time.sleep(DELAY_BETWEEN_CLICKS_SECONDS)
    
    print("Saare coordinates par click ho gaya.")
    return True # Indicate clicks were performed

if __name__ == "__main__":
    print("Auto Clicker shuru ho gaya hai.")
    print(f"Har click ke beech {DELAY_BETWEEN_CLICKS_SECONDS} seconds ka delay.")
    print(f"Poora sequence har {DELAY_BETWEEN_LOOPS_HOURS} ghante mein repeat hoga.")
    print("Script band karne ke liye Ctrl+C dabayein (terminal mein).")

    try:
        # Pehle check karein ki virtual environment activate hai ya nahi (optional, par acchi practice)
        import os
        if not os.environ.get('VIRTUAL_ENV'):
            print("\nWARNING: Aap shayad virtual environment ke bahar hain.")
            print("Behtar hoga ki aap virtual environment activate karke script run karein:")
            print("  . myenv/bin/activate  (agar environment ka naam 'myenv' hai)")
            print("Yaad rakhein ki 'pynput' usi environment mein install hona chahiye.\n")


        while True:
            clicks_performed = perform_click_sequence()
            if not clicks_performed and not coordinates_to_click: # Agar koi coordinate nahi tha
                break # Loop se bahar aa jao

            print(f"Sequence poora hua. Agle loop ke liye {DELAY_BETWEEN_LOOPS_HOURS} ghante intezar...")
            time.sleep(delay_between_loops_seconds)
            
    except KeyboardInterrupt:
        print("\nAuto Clicker user dwara band kiya gaya.")
    except ImportError:
        print("\nError: 'pynput' module nahi mila.")
        print("Kripya pehle 'pynput' install karein:")
        print("  pip install pynput (agar virtual environment activate hai)")
        print("Ya phir apne system ke Python environment ke liye install karein.")
    except Exception as e:
        print(f"Ek anayatha error aayi: {e}")
