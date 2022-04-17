from tkinter import *
from tkinter import ttk
from pokeapi import get_pokemon_info


def main():

    root =Tk()
    root.title("pokemon Info viewer")
    root.iconbitmap("pokeball_icon.ico")
    root.geometry("400x400")


    frm_user_input = ttk.Frame(root)
    frm_user_input.grid(row=0, column=0, columnspan=2)

    frm_info = ttk.LabelFrame(root, text='Info')
    frm_info.grid(row=1, column=0)

    frm_stats = ttk.LabelFrame(root, text='Stats')
    frm_stats.grid(row=1, column=1)


    lbl_name = ttk.Label(frm_user_input, text='Pokemon Name')
    lbl_name.grid(row=1, column=1)

    ent_name = ttk.Entry(frm_user_input)
    ent_name.grid(row=1, column=2)

    def btn_get_info_click():

        pokemon_name = ent_name.get()
        poke_dict = get_pokemon_info(pokemon_name)
        
        if poke_dict:
            lbl_height_val['text'] = str(poke_dict['height']) + ' dm'
            #lbl_type_val['text']   =

    btn_get_info =ttk.Button(frm_user_input, text='Get Info', command=btn_get_info_click)
    btn_get_info.grid(row=1, column=3)


    lbl_height = ttk.Label(frm_info, text='Height:')
    lbl_height.grid(row=100, column=100)
    lbl_height_val = ttk.Label(frm_info, text='TBD')
    lbl_height_val.grid(row=100, column=200)

    lbl_type = ttk.Label(frm_info, text='Type:')
    lbl_type.grid(row=300, column=100)
    lbl_type_val = ttk.Label(frm_info, text='TBD')
    lbl_type_val.grid(row=300, column=200)
    
    
    root.mainloop()



main()