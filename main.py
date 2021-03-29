import tkinter as tk
from datetime import datetime
from tkinter import scrolledtext


def window_tk():
    date_now = datetime.now().date()
    time_now = datetime.now().time()
    prior_error = "ERROR"
    prior_debug = "DEBUG"
    prior_trace = "TRACE"
    str_error = "Error occured"
    str_debug = "DEBUG mode"
    str_trace = "Tracing"

    window = tk.Tk()
    window.title("Lab 2")
    window.geometry('430x400')

    label_name = tk.Label(text="Имя файла:")
    label_name.grid(column=0, row=0, sticky="w", padx=5, pady=5)

    file_name = tk.StringVar()
    entry_name = tk.Entry(textvariable=file_name)
    entry_name.grid(column=1, row=0, padx=5, pady=5)

    label_format = tk.Label(text="Формат сообщения:")
    label_format.grid(column=0, row=1, sticky="w", padx=5, pady=5)

    label_format_example = tk.Label(text="Пример формата: {prior} {data} {time} {message}")
    label_format_example.grid(column=0, row=2, columnspan=3, sticky="w", padx=5, pady=5)

    file_format = tk.StringVar()
    entry_format = tk.Entry(textvariable=file_format)
    entry_format.grid(column=1, row=1, padx=5, pady=5)

    def click_button_error(file_format2="", name=""):
        file_format2 = file_format2 + file_format.get()
        name = name + file_name.get()
        form = file_format2.format(message=str_error, data=date_now, time=time_now, prior=prior_error)
        result.insert(1.0, form + '\n')
        print(form + '\n')
        f = open('C:/Users/Dima/Downloads/' + name + '.csv', 'a')
        f.write(form + '\n')
        f.close()

    def click_button_debug(file_format2="", name=""):
        file_format2 = file_format2 + file_format.get()
        name = name + file_name.get()
        form = file_format2.format(message=str_debug, data=date_now, time=time_now, prior=prior_debug)
        result.insert(1.0, form + '\n')
        print(form + '\n')
        f = open('C:/Users/Dima/Downloads/' + name + '.csv', 'a')
        f.write(form + '\n')
        f.close()

    def click_button_trace(file_format2="", name=""):
        file_format2 = file_format2 + file_format.get()
        name = name + file_name.get()
        form = file_format2.format(message=str_trace, data=date_now, time=time_now, prior=prior_trace)
        result.insert(1.0, form + '\n')
        print(form + '\n')
        f = open('C:/Users/Dima/Downloads/' + name + '.csv', 'a')
        f.write(form + '\n')
        f.close()

    button_error = tk.Button(
        text="Error",
        width=6,
        height=2,
        command=click_button_error
    )
    button_error.grid(column=0, row=3, sticky="w", padx=5, pady=5)

    button_debug = tk.Button(
        text="Debug",
        width=6,
        height=2,
        command=click_button_debug
    )
    button_debug.grid(column=1, row=3, sticky="w", padx=5, pady=5)

    button_trace = tk.Button(
        text="Trace",
        width=6,
        height=2,
        command=click_button_trace
    )
    button_trace.grid(column=2, row=3, sticky="w", padx=5, pady=5)

    result = scrolledtext.ScrolledText(window, width=50, height=15)
    result.grid(column=0, row=4, columnspan=3, padx=5, pady=5)

    window.mainloop()


if __name__ == '__main__':
    window_tk()
