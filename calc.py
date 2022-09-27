import tkinter as tk

window = tk.Tk()

lbl_calc_resualt = tk.Label(
    window,
    text = "0",
    width = 30,
    height= 3
)

lbl_calc_resualt.grid(row = 0, column = 0, columnspan= 4)

def is_last_number_decimal(number):
    
    for char in number[::-1]:
        if char == ".":
            return True
        if char in ["+", "-", "*"]:
            return False
        
    return False

last_op_index = -1
last_dot_index = -1

def insert_number_in_calc_resualt(btn_text):
    
    current = lbl_calc_resualt["text"]
    
    global last_op_index, last_dot_index
    
    if btn_text in ["+", "-", "*"]:
        last_op_index = len(current)
    if btn_text == "C":
        lbl_calc_resualt["text"] = "0"
        last_op_index, last_dot_index = 0, 0
    elif current == "0":
        lbl_calc_resualt["text"] = btn_text
    elif btn_text == "=":
        result = str(eval(current))
        lbl_calc_resualt["text"] = result
        last_op_index, last_dot_index = 0, 0
        if "." in result:
            last_dot_index = result.index(".")
    else:
        if btn_text == ".":
            if last_dot_index > last_op_index:
                pass
            elif current[-1] == ".":
                pass
            else:
                 lbl_calc_resualt["text"] += btn_text
                 last_dot_index = len(current) 
        elif btn_text == "+" or btn_text == "-" or btn_text == "*" :
            if current[-1] == "+" or current[-1] == "-" or current[-1] == "*":
                lbl_calc_resualt["text"] = current[:-1] + btn_text
            else:
                lbl_calc_resualt["text"] += btn_text
        else:
            lbl_calc_resualt["text"] += btn_text
    
calc_keys = [
    {
        "text": "7",
        "command": lambda : insert_number_in_calc_resualt("7")
    },
     {
        "text": "8",
        "command": lambda : insert_number_in_calc_resualt("8")
    },
      {
        "text": "9",
        "command": lambda : insert_number_in_calc_resualt("9")
    },
       {
        "text": "+",
        "command": lambda : insert_number_in_calc_resualt("+")
    },
       {
        "text": "4",
        "command": lambda : insert_number_in_calc_resualt("4")
    },
       {
        "text": "5",
        "command": lambda : insert_number_in_calc_resualt("5")
    },
       {
        "text": "6",
        "command": lambda : insert_number_in_calc_resualt("6")
    },
       {
        "text": "-",
        "command": lambda : insert_number_in_calc_resualt("-")
    },
       {
        "text": "1",
        "command": lambda : insert_number_in_calc_resualt("1")
    },
       {
        "text": "2",
        "command": lambda : insert_number_in_calc_resualt("2")
    },
       {
        "text": "3",
        "command": lambda : insert_number_in_calc_resualt("3")
    },
       {
        "text": "*",
        "command": lambda : insert_number_in_calc_resualt("*")
    },
       {
        "text": ".",
        "command": lambda : insert_number_in_calc_resualt(".")
    },
       {
        "text": "0",
        "command": lambda : insert_number_in_calc_resualt("0")
    },
       {
        "text": "C",
        "command": lambda : insert_number_in_calc_resualt("C")
    },
       {
        "text": "=",
        "command": lambda : insert_number_in_calc_resualt("=")
    }
]

calc_keys_objs = []

for calc_keys_data in calc_keys:
    
    btn = tk.Button(
        master = window,
        text = calc_keys_data["text"],
        command = calc_keys_data["command"],
        height=3,
    )
    calc_keys_objs.append(btn)

for i, calc_keys_obj in enumerate(calc_keys_objs):
    
    calc_keys_obj.grid(row = (i // 4) + 1, column = i % 4, sticky = "wnes")

lbl_made = tk.Label(
    master = window, 
    text = "made by m.seyf8"
)

lbl_made.grid(row = 6 , column = 0, columnspan = 4)

window.title("Calculator")

window.mainloop()