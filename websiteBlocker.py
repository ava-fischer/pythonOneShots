import tkinter as tk

root = tk.Tk()
root.geometry("500x300") #dimensions of the UI window; x by y
root.resizable(0, 0)
root.title("Website Blocker") #name of the UI window

tk.Label(root, text = "Website Blocker", font = "arial 20 bold").pack() #font may also be entered as tuple ex. font = (Arial, 20)
#Label(root, text = "Ava Fischer", font = "arial 20 bold").pack(side=BOTTOM)

host_path = 'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

tk.Label(root, text ='Enter Website :' , font ='arial 13 bold').place(x = 5 , y = 60)
Websites = tk.Text(root, font = 'arial 10', height = '2', width = '40', wrap = tk.WORD, padx = 5, pady = 5) #height is given in lines
Websites.place(x= 140, y = 60)

def Blocker():
    website_lists = Websites.get(1.0, tk.END)
    Website = list(website_lists.split(","))

    #alreadyBlocked.pack_forget()
    #wasBlocked.pack_forget()

    with open(host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                alreadyBlocked = tk.Label(root, text = website + " has already been blocked!" , font = 'arial 12 bold').place(x = 160, y = 200)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                wasBlocked = tk.Label(root, text = website + " was blocked!", font = 'arial 12 bold').place(x = 230, y = 200)
                Websites.delete(1.0, tk.END)

block_btn = tk.Button(root, text = 'BLOCK', font = 'arial 12 bold', command = Blocker, width = 6, bg = 'royal blue1', activebackground = 'sky blue')
block_btn.place(x = 230, y = 150)

root.mainloop()