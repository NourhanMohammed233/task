import tkinter as tk
from gtts import gTTS
import pyttsx3
import os

# تهيئة pyttsx3
engine = pyttsx3.init()

# الوظائف المرتبطة بالأزرار
def play_text_gtts():
    text = entry.get()
    if text.strip():  # التأكد من أن النص غير فارغ
        tts = gTTS(text=text, lang="en")
        tts.save("output.mp3")
        os.system("start output.mp3")  # تشغيل الملف الصوتي

def play_text_pyttsx3():
    text = entry.get()
    if text.strip():  # التأكد من أن النص غير فارغ
        engine.say(text)
        engine.runAndWait()

def clear_entry():
    entry.delete(0,tk.END)  # لحذف الكلام ف ال entry Set

def exit_app():
    root.destroy()  # إغلاق التطبيق

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("Text-to-Speec")
root.geometry("400x400")  # تحديد حجم النافذة
root.config(bg="lightblue")

# العنوان
label = tk.Label(root, text="Text-to-Speech", font=("Helvetica", 16),bg="lightblue",fg="blue")
label.pack(pady=20)

# مربع إدخال النص
entry = tk.Entry(root, width=40)
entry.pack(pady=20)

# إطار للأزرار
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# زر Play باستخدام gTTS
button1 = tk.Button(button_frame, text="Play sound from Google", width=20, command=play_text_gtts,bg="pink")
button1.grid(row=0, column=0, padx=5)

# زر Play باستخدام pyttsx3
button2 = tk.Button(button_frame, text="Play sound from window", width=20, command=play_text_pyttsx3,fg="purple")
button2.grid(row=1, column=0, padx=5)

# زر Set
button3 = tk.Button(button_frame, text="Set", width=10, command=clear_entry,bg="gray")
button3.grid(row=2, column=0, pady=10)

# زر Exit
button4 = tk.Button(button_frame, text="Exit", width=10, command=exit_app, bg="red")
button4.grid(row=3, column=0, pady=10)

# تشغيل التطبيق
root.mainloop()