from tkinter import messagebox
import pandas as pd
from tkinter import *
from pandastable import Table

new_dict = {"website": []}


def panda_dict(new_dict):
    try:
        json_data = pd.read_json("userFiles/data.json")
    except (ValueError, FileNotFoundError):
        messagebox.showinfo(title="Oops", message="Please make sure you have some data")
    else:
        data_dict = json_data.to_dict()
        for data_key, dict_value in data_dict.items():
            new_dict["website"].append(data_key)
            for key, values in dict_value.items():
                new_dict[key] = []
        for dict_value in data_dict.values():
            for key, values in dict_value.items():
                new_dict[key].append(values)
    return new_dict


def data_table():
    new_dict = {"website": []}
    formated_dict = panda_dict(new_dict)
    df = pd.DataFrame.from_dict(formated_dict)
    return df


class TableData():
    """Basic test frame for the table"""

    def __init__(self,df):
        table_window = Tk()
        # table_window.geometry('600x400')
        table_window.title('Table app')
        f = Frame(table_window)
        f.grid()
        self.table = pt = Table(f, dataframe=df, )  # showtoolbar=True, showstatusbar=True)
        pt.show()
        return
