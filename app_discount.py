# 引入 tkinter 模組，始用別名 tk 代表 tkinter，可以少打字
import tkinter as tk

# 建立主視窗，建立 Tk 物件實例
window = tk.Tk()

# 設定視窗標題

window.title('Discount Calculator')
# 設定背景顏色為白色
window.configure(background='white')

# 建立商品價格輸入
good_label = tk.Label(text='請輸入商品價格')
# 渲染輸入框
good_label.pack()

# 建立輸入框
good_input_entry = tk.Entry(window)
# 渲染輸入框
good_input_entry.pack()

# 建立折扣數輸入
discount_label = tk.Label(text='請輸入折扣數')
# 渲染輸入框
discount_label.pack()

# 建立輸入框
discount_input_entry = tk.Entry(window)
# 渲染輸入框
discount_input_entry.pack()

# 建立顯示結果文字，先顯示空白
result_label = tk.Label(text='')
# 渲染
result_label.pack()

def price(good,discount):
    return good*discount*0.1

def click_me():
    # 取出 input 值
    good = int(good_input_entry.get())
    discount = int(discount_input_entry.get())
    # 顯示在 Label 元件上
    message=price(good,discount)
    result_label.configure(text="折扣後的商品價格為"+str(message))

# 建立按鈕元件（第一個參數放入 window 代表要顯示在哪個區塊），顯示文字為 click me，command 是當點擊會觸發處理的函式
button = tk.Button(window, text='click me', command=click_me)
# 渲染按鈕元件
button.pack()

# 運行主程式，最後一定要運行 window.mainloop()，讓 window 不斷地重新整理
# 這部份可以想成是電影或是動畫，事實上是不斷翻頁，所以就是一個 while 迴圈的感覺 
window.mainloop()