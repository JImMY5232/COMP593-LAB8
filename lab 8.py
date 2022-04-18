from tkinter import *
from tkinter import ttk
import types
from pokeapi import get_pokemon_info


def main():

    root =Tk()
    root.title("pokemon Information")
    root.iconbitmap("pokeball_icon.ico")
    root.geometry("600x300")


    frm_user_input = ttk.Frame(root)
    frm_user_input.grid(row=0, column=1, columnspan=2, padx=20, pady=(20))

    frm_info = ttk.LabelFrame(root, text='Info')
    frm_info.grid(row=1, column=1,padx=20, pady=(5,45))

    frm_stats = ttk.LabelFrame(root, text='Stats')
    frm_stats.grid(row=1, column=2, padx=10, pady=20)


    lbl_name = ttk.Label(frm_user_input, text='Pokemon Name')
    lbl_name.grid(row=1, column=1)

    ent_name = ttk.Entry(frm_user_input)
    ent_name.grid(row=1, column=2)
    #get function
    def btn_get_info_click():

        pokemon_name = ent_name.get()
        poke_dict = get_pokemon_info(pokemon_name)
        
        if poke_dict:
            lbl_height_val['text'] = str(poke_dict['height']) + ' dm'
            lbl_weight_val['text'] = str(poke_dict['weight']) + ' hg'
            types_list = (t['type']['name']for t in poke_dict['types'])
            lbl_type_val['text']   = ', '.join(types_list)
            prg_hp['value'] = poke_dict['stats'][0]['base_stat']
            prg_attack['value'] = poke_dict['stats'][1]['base_stat']
            prg_defence['value'] = poke_dict['stats'][2]['base_stat']
            prg_splattack['value'] = poke_dict['stats'][3]['base_stat']
            prg_spldefence['value'] = poke_dict['stats'][4]['base_stat']
            prg_speed['value'] = poke_dict['stats'][5]['base_stat']

    #button
    btn_get_info =ttk.Button(frm_user_input, text='Get Info', command=btn_get_info_click)
    btn_get_info.grid(row=1, column=3)

    #info box
    lbl_height = ttk.Label(frm_info, text='Height:')
    lbl_height.grid(row=100, column=100, padx=10, pady=10, sticky=E)
    lbl_height_val = ttk.Label(frm_info, width=20)
    lbl_height_val.grid(row=100, column=200, padx=10, pady=1, sticky=W)

    lbl_weight = ttk.Label(frm_info, text='Weight:')
    lbl_weight.grid(row=200, column=100, padx=10, pady=6, sticky=E)
    lbl_weight_val = ttk.Label(frm_info,  width=20)
    lbl_weight_val.grid(row=200, column=200, padx=10, pady=1, sticky=W)

    lbl_type = ttk.Label(frm_info, text='Type:')
    lbl_type.grid(row=300, column=100, padx=10, pady=8, sticky=E)
    lbl_type_val = ttk.Label(frm_info,  width=20)
    lbl_type_val.grid(row=300, column=200, padx=10, pady=1, sticky=W)

    #stats box
    lbl_hp =ttk.Label(frm_stats, text='HP:')
    lbl_hp.grid(row=100, column=100, padx=10, pady=1, sticky=E)
    prg_hp =ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_hp.grid(row=100, column=200, padx=10, pady=1, sticky=W)

    lbl_attack =ttk.Label(frm_stats, text='Attack:')
    lbl_attack.grid(row=200, column=100, padx=10, pady=1, sticky=E)
    prg_attack =ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_attack.grid(row=200, column=200, padx=10, pady=1, sticky=W)

    lbl_defence =ttk.Label(frm_stats, text='Defence:')
    lbl_defence.grid(row=300, column=100, padx=10, pady=1, sticky=E)
    prg_defence =ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_defence.grid(row=300, column=200, padx=10, pady=1, sticky=W)

    lbl_splattack =ttk.Label(frm_stats, text='Special Attack:')
    lbl_splattack.grid(row=400, column=100, padx=10, pady=1, sticky=E)
    prg_splattack =ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_splattack.grid(row=400, column=200, padx=10, pady=1, sticky=W)

    lbl_spldefence =ttk.Label(frm_stats, text='Special Defence:')
    lbl_spldefence.grid(row=500, column=100, padx=10, pady=1, sticky=E)
    prg_spldefence =ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_spldefence.grid(row=500, column=200, padx=10, pady=1, sticky=W)
    
    lbl_speed =ttk.Label(frm_stats, text='Speed:')
    lbl_speed.grid(row=600, column=100, padx=10, pady=1, sticky=E)
    prg_speed =ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_speed.grid(row=600, column=200, padx=10, pady=1, sticky=W)
    
    
    root.mainloop()



main()