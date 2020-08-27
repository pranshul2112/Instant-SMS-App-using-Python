import requests
import json
from tkinter import *
from  tkinter.messagebox import showinfo, showerror

def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'kMFxluvieyEtjPBK06ZbdA95pTOV4m7XozasI3DSNCJ1hUwqGHIyTpPV4Ak2RHviJhjCwEmN0r56XFgZ',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')


def button_click():
    num = textNumber.get()
    msg = textMessage.get("1.0", END)
    r = send_sms(num, msg)
    if r:
       showinfo("Success", "Message sent successfully")
    else:
        showerror("Error", "Message not sent")



root = Tk()
root.title("Message Sender")
root.geometry("400x550")
font = ("Helvetica", 20, "bold")

textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)

textMessage = Text(root)
textMessage.pack(fill= X)
sendButton = Button(root, text="SEND SMS", command=button_click)
sendButton.pack()

root.mainloop()
