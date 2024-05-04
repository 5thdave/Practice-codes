import tkinter as tk

def Addbutton():
    a = Display1.get()
    b = [int(x) for x in a]
    print(b)
    r = sum(b)

    #b = Display2.get()
    #r = int(a)+int(b)

    answer = tk.Label(frame2, text = (f"{r}"), fg = "#ffffff", bg = "#00FFFF", font = ("Arial", 20))
    answer.pack(pady= 40, side=tk.RIGHT)
def Subbutton():
    a = Display1.get()
    b = Display2.get()
    r = int(a)-int(b)
    answer = tk.Label(frame2, text = (f"{r}"), fg = "#ffffff", bg = "#00FFFF", font = ("Arial", 20))
    answer.pack(pady= 40, side=tk.RIGHT)   
def Dividebutton():
    a = Display1.get()
    b = Display2.get()
    r = int(a)/int(b)
    answer = tk.Label(frame2, text = (f"{r}"), fg = "#ffffff", bg = "#00FFFF", font = ("Arial", 20))
    answer.pack(pady= 40, side=tk.RIGHT)   
def Multiplybutton():
    a = Display1.get()
    b = Display2.get()
    r = int(a)*int(b)
    answer = tk.Label(frame2, text = (f"{r}"), fg = "#ffffff", bg = "#00FFFF", font = ("Arial", 20))
    answer.pack(pady= 40, side=tk.RIGHT)       


root = tk.Tk()
root.configure(background="#00FFFF")
root.title("Calculator")
root.geometry("500x700")

frame0 = tk.Frame(root,bg ="#00FFFF")
Display1 = tk.Entry(frame0, fg = "#ffffff", bg = "#00FFFF", font = ("Arial", 20))
Display1.pack(padx=20,pady= 40 , side=tk.LEFT)
#Display2 = tk.Entry(frame0, fg = "#ffffff", bg = "#00FFFF", font = ("Arial", 20))
#Display2.pack(pady= 40, side=tk.RIGHT)
frame0.pack()

frame2 = tk.Frame(root,bg ="#00FFFF")
equalsign = tk.Label(frame2, text = ("="), fg = "#ffffff", bg = "#00FFFF", font = ("Arial", 20))
equalsign.pack(padx=20,pady= 40 , side=tk.LEFT)
frame2.pack()

frame1 = tk.Frame(root, bg="#00FFFF")
Add_bttn = tk.Button(frame1, text= ("+"), fg = "#ffffff", bg = "#00FFFF", font=("Arial", 20) , command = Addbutton)
Add_bttn.pack(padx=10 ,pady=10 , side = tk.LEFT)
Sub_bttn = tk.Button(frame1, text= ("-"), fg = "#ffffff", bg = "#00FFFF", font=("Arial", 20) , command = Subbutton )
Sub_bttn.pack(pady=10 , side = tk.RIGHT)
frame1.pack()

frame1 = tk.Frame(root, bg="#00FFFF")
Divide_bttn = tk.Button(frame1, text= ("/"), fg = "#ffffff", bg = "#00FFFF", font=("Arial", 20) , command = Dividebutton)
Divide_bttn.pack(padx=10 ,pady=10 , side = tk.LEFT)
Multiply_bttn = tk.Button(frame1, text= ("X"), fg = "#ffffff", bg = "#00FFFF", font=("Arial", 20) , command = Multiplybutton )
Multiply_bttn.pack(pady=10 , side = tk.RIGHT)
frame1.pack()
root.mainloop()