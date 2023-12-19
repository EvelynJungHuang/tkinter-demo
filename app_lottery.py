import tkinter as tk
import math

window = tk.Tk()
window.title('發票 App')
window.geometry('800x600')
window.configure(background='white')

header_label = tk.Label(window, text='發票對獎')
header_label.pack()

lottery_frame = tk.Frame(window)
lottery_frame.pack(side=tk.TOP)
lottery_label = tk.Label(lottery_frame, text='中獎數字後三碼')
lottery_label.pack(side=tk.LEFT)
lottery_entry = tk.Entry(lottery_frame)
lottery_entry.pack(side=tk.LEFT)

ticket_frame = tk.Frame(window)
ticket_frame.pack(side=tk.TOP)
ticket_label = tk.Label(ticket_frame, text='發票後三碼')
ticket_label.pack(side=tk.LEFT)
ticket_entry = tk.Entry(ticket_frame)
ticket_entry.pack(side=tk.LEFT)

array_frame = tk.Frame(window)
array_frame.pack(side=tk.TOP)
arraymean_label = tk.Label(array_frame,text='中獎號碼序列：')
arraymean_label.pack(side=tk.LEFT)
arraynumber_label = tk.Label(array_frame, text='')
arraynumber_label.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

array_number=[]
def enter_number():
    lottery_number = lottery_entry.get()
    array_number.append(lottery_number)
    lottery_entry.delete(0, 'end')
    arraynumber_label.configure(text=array_number) 
    
def matching():
    if ticket_entry.get() in array_number:
        result_label.configure(text='恭喜中獎') 
    else:
        result_label.configure(text='抱歉沒有中獎') 

lottery_btn = tk.Button(lottery_frame, text='輸入', command=enter_number)
lottery_btn.pack()
matching_btn = tk.Button(window, text='馬上對獎', command=matching)
matching_btn.pack()



window.mainloop()