import tkinter as tk
from tkinter import ttk,scrolledtext, messagebox as msg
from Currency_Exchange import CurrencyExchange

win = tk.Tk()
CE = CurrencyExchange()

#creating menus as tabs
menus = ('Exchange','Add New','View Rates','Primary','Update Rates')
tabControl = ttk.Notebook(win)
tabs = [ttk.Frame(tabControl) for x in menus]
for i in range(len(menus)):
	tabControl.add(tabs[i], text = menus[i])
tabControl.pack(expand=1,fill='both')

#inner frames
lbls = ('Currency Conversion','Add New Currency','Exchange Rates','Change Primary Currency', 'Update Rate')
mega = []
for i in range(len(lbls)):
	mega.append(ttk.LabelFrame(tabs[i], text = lbls[i]))
	mega[i].grid(column = 0,row = 0, padx = 20,pady = 20)
	
f = ('Times new roman',8,'bold')

def click():
	if amnt_frm.get() == '' or (not amnt_frm.get().isdigit()):
		return
	amnt = '{:,.2f}'.format(CE.exchange(cur_frm.get(),cur_to.get(),float(amnt_frm.get())))
	amnt_to.set(amnt)

def combo_update(index, value, op):
	if (not cur_frm.get()) or (not cur_to.get()):
		return
	click()

def add_currency():
	cn = cur_name.get().upper()
	cv = cur_val.get()
	try:
		cv = float(cv)
	except:
		msg.showinfo('Invalid Input','Value must be in Digits')
		return
	if CE.add_currency(cn,cv):
		msg.showinfo('Add Currency','Currency added Successfully!')
		CE.save()
		refresh_rates()
	
def update_rate():
	cv = new_cur_val.get()
	try:
		cv = float(cv)
	except:
		msg.showinfo('Invalid Input','Value must be in Digits')
		return
	if CE.change_rate(cur.get(), cv):
		msg.showinfo('Update Currency Rate','Currency Rate updated Successfully!')
		CE.save()
		refresh_rates()

def change_primary():
	pri = pri_cur.get()
	if CE.set_primary(pri):
		msg.showinfo('Primary Currency','Primary Currency set Successfully!')
		CE.save()
		refresh_rates()
		lbl1.configure(text = 'Unit Value in ' + CE.primary)
		lbl2.configure(text = 'Unit Value in ' + CE.primary)
	
def refresh_rates():
	scrt.configure(state = 'normal')
	scrt.delete('1.0', tk.END)
	scrt.insert('1.0',CE.get_All())
	scrt.configure(state = 'disabled')	
	
#first tab line 76 - 104

#adding labels
ttk.Label(mega[0],text = 'Currency', font = f).grid(column = 0,row=1, padx = 3, sticky = 'W')
ttk.Label(mega[0],text = 'Amount', font = f).grid(column = 0,row=2,padx = 3, stick = 'W')
ttk.Label(mega[0],text = 'From', font = f).grid(column = 1,row=0, padx = 3)
ttk.Label(mega[0],text = 'To', font = f).grid(column = 3,row=0, padx = 3)

#adding combo boxes
frm = tk.StringVar()
frm.trace('w', combo_update)
cur_frm = ttk.Combobox(mega[0],width=11,textvariable = frm, values = list(CE.currencies.keys()), state = 'readonly')
cur_frm.grid(column = 1,row = 1, padx = 3)
to = tk.StringVar()
to.trace('w', combo_update)
cur_to = ttk.Combobox(mega[0],width=11,textvariable = to, values = list(CE.currencies.keys()), state = 'readonly')
cur_to.grid(column = 3,row = 1, padx = 3)

#adding button
action = ttk.Button(mega[0],text = 'Calculate',command = click)
action.grid(column = 2,row = 3,padx=5,pady = 10)

#adding text box
amnt_frm = tk.StringVar()
txtB = ttk.Entry(mega[0],width = 12,textvariable = amnt_frm)
txtB.grid(column = 1,row = 2)
amnt_to = tk.StringVar()
txtB = ttk.Entry(mega[0],width = 12,textvariable = amnt_to, state = 'readonly', font = f)
txtB.grid(column = 3,row = 2)

#Second Tab line 106 - 123

#Labels
ttk.Label(mega[1],text = 'Currency Name', font = f).grid(column = 0,row=0, padx = 5, pady = 5, sticky = 'W')
lbl1 = ttk.Label(mega[1],text = 'Unit Value in ' + CE.primary, font = f)
lbl1.grid(column = 0,row=1,padx = 5, pady = 5, sticky = 'W')

#text boxes
cur_name = tk.StringVar()
txtB = ttk.Entry(mega[1],width = 12,textvariable = cur_name)
txtB.grid(column = 1,row = 0, padx = 5, pady = 5)
cur_val = tk.StringVar()
txtB = ttk.Entry(mega[1],width = 12,textvariable = cur_val, font = f)
txtB.grid(column = 1,row = 1, padx = 5, pady = 5)

#adding button
add_cur = ttk.Button(mega[1],text = 'Add Currency',command = add_currency)
add_cur.grid(column = 0,row = 2,padx=5, pady = 5, columnspan = 2, sticky = 'NEWS')

#third tab line 125 - 130

#adding scrolled text
scrt = scrolledtext.ScrolledText(mega[2],width = 40,height = 50, wrap = tk.WORD)
scrt.grid(row = 4,column = 0,columnspan = 3,pady=10, padx = 10)
refresh_rates()

#fourth tab line 132 - 140

#Label
ttk.Label(mega[3],text = 'Choose Currency', font = f).grid(column = 0,row=0, padx = 10, pady = 10, sticky = 'W')
#combobox
pri_cur = tk.StringVar()
ttk.Combobox(mega[3],width=11,textvariable = pri_cur, values = list(CE.currencies.keys()), state = 'readonly').grid(column = 1,row = 0, padx = 5)
#button
ttk.Button(mega[3],text = 'Set to Primary',command = change_primary).grid(column = 0,row = 2,padx=5, pady = 5, columnspan = 2, sticky = 'NEWS')

#fifth tab line 142 - 156

#Labels
ttk.Label(mega[4],text = 'Choose Currency', font = f).grid(column = 0,row=0, padx = 5, pady = 5, sticky = 'W')
lbl2 = ttk.Label(mega[4],text = 'Unit Value in ' + CE.primary, font = f)
lbl2.grid(column = 0,row=1,padx = 5, pady = 5, sticky = 'W')

#text box and combo box
cur = tk.StringVar()
ttk.Combobox(mega[4],width=11,textvariable = cur, values = list(CE.currencies.keys()), state = 'readonly').grid(column = 1,row = 0, padx = 3)
new_cur_val = tk.StringVar()
ttk.Entry(mega[4],width = 12,textvariable = new_cur_val, font = f).grid(column = 1,row = 1, padx = 5, pady = 5)

#adding button
ttk.Button(mega[4],text = 'Update Rate',command = update_rate).grid(column = 0,row = 2,padx=5, pady = 5, columnspan = 2, sticky = 'NEWS')

win.mainloop()