from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:  # Sirf jab button press ho tabhi action lena hai
        print(f"Mouse clicked at: (X={x}, Y={y})")
        # Agar aap chahte hain ki ek click ke baad script band ho jaye, toh yahan 'return False' likh dein
        # return False

print("Screen par click karein coordinates janne ke liye.")
print("Script band karne ke liye Ctrl+C dabayein.")

# Listener start karein
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

print("Listener stopped.")

