import tkinter as tk
import pandas as pd

Results = []



def Displayresult():    
    Name = Name_box.get()
    Age = Age_box.get()
    Maths = Maths_box.get()
    Eng = Eng_box.get()
    Phy = Phy_box.get()
    Chem = Chem_box.get()
    Bio = Bio_box.get()

    Age = int(Age)
    Maths = int(Maths)
    Eng = int(Eng)
    Phy = int(Phy)
    Chem = int(Chem)
    Bio = int(Bio)
    Total = Maths+Eng+Phy+Chem+Bio
    average = Total/5
    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"
    Database = {"Name":Name,"Age":Age,"Maths":Maths,"Eng":Eng,"Phy":Phy,"Chem":Chem,"Bio":Bio,"Total":Total,\
        "Average":average,"Grade":grade}
    Results.append(Database)
    pt = pd.DataFrame(Results)
    
    frame8 = tk.Frame(root, bg = "#00FFFF")
    #Display_head = tk.Label(frame8, bg = "#00FFFF" , text = ("Name\t\t\tAge\tMaths\tEng\tPhy\tChem\tBio\tTotal\tAverage\tGrade") , fg = "#ffffff" , font = ("Arial 10"))
    #Display_head.pack(pady = 10)
    Display_result = tk.Label(frame8, bg = "#00FFFF" , text = f"{pt}", fg = "#ffffff" , font = ("Arial 30"))
    Display_result.pack(pady = 10)
    #print = tk.Button(frame8, bg="#00FFFF",text="Printresult",fg="#ffffff", font=("Arial 20"), command = Print)
    #print.pack()

    frame8.pack()

#def Print():
    
    

root= tk.Tk()
root.geometry("2000x2000")
root.title("Result Checker")
root.configure(background="#00FFFF")

frame1 = tk.Frame(root, bg="#00FFFF")
Name_txt = tk.Label(frame1, text="Name: ", fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Name_txt.pack(padx=10,pady=10 , side=tk.LEFT)
Name_box = tk.Entry(frame1, fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Name_box.pack(pady=10 , side=tk.RIGHT)
frame1.pack()

frame2 = tk.Frame(root, bg="#00FFFF")
Age_txt = tk.Label(frame2, text="Age: ", fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Age_txt.pack(padx=10,pady=10 , side=tk.LEFT)
Age_box = tk.Entry(frame2, fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Age_box.pack(pady=10 , side=tk.RIGHT)
frame2.pack()

frame3 = tk.Frame(root, bg="#00FFFF")
Maths_txt = tk.Label(frame3, text="Maths: ", fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Maths_txt.pack(padx=10,pady=10 , side=tk.LEFT)
Maths_box = tk.Entry(frame3, fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Maths_box.pack(pady=10 , side=tk.RIGHT)
frame3.pack()

frame4 = tk.Frame(root, bg="#00FFFF")
Eng_txt = tk.Label(frame4, text="Eng: ", fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Eng_txt.pack(padx=10,pady=10 , side=tk.LEFT)
Eng_box = tk.Entry(frame4, fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Eng_box.pack(pady=10 , side=tk.RIGHT)
frame4.pack()

frame5 = tk.Frame(root, bg="#00FFFF")
Phy_txt = tk.Label(frame5, text="Phy: ", fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Phy_txt.pack(padx=10,pady=10 , side=tk.LEFT)
Phy_box = tk.Entry(frame5, fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Phy_box.pack(pady=10 , side=tk.RIGHT)
frame5.pack()

frame6 = tk.Frame(root, bg="#00FFFF")
Chem_txt = tk.Label(frame6, text="Chem: ", fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Chem_txt.pack(padx=10,pady=10 , side=tk.LEFT)
Chem_box = tk.Entry(frame6, fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Chem_box.pack(pady=10 , side=tk.RIGHT)
frame6.pack()

frame7 = tk.Frame(root, bg="#00FFFF")
Bio_txt = tk.Label(frame7, text="Bio: ", fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Bio_txt.pack(padx=10,pady=10 , side=tk.LEFT)
Bio_box = tk.Entry(frame7, fg="#ffffff",bg="#00FFFF",font=("Arial 20"))
Bio_box.pack(pady=10 , side=tk.RIGHT)
frame7.pack()

Display_txt = tk.Button(root, bg="#00FFFF",text="Display Result",fg="#ffffff", font=("Arial 20"), command=Displayresult)
Display_txt.pack(pady=20)

root.mainloop()