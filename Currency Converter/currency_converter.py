from tkinter import *
from tkinter import ttk
import requests
import tkinter.font as font

country = {'USD':"United_States_dollar", 'AED':"United_Arab_Emeriates_dirham", 'ARS':'Argentine_peso',   'AUD':'Australian_dollar',
           'BGN':'Bulgarian_lev',        'BRL':'Brazilian_real',               'BSD':'Bahamian_Dollar',  'CAD':'Bahamian_doller',
           'CHF':'Canadian_doller',      'CLP':'Chilean_peso',                 'CNY':'Chinese_yuan',     'COP':'Colombian_peso',
           'CZK':'Czech_koruna',         'DKK':'Denmark',                      'DOP':'Dominican_peso',   'EGP':'Egyptian_pound',
           'EUR':'EURO',                 'FJD':'Fijian_doller',                'GBP':'British_pound',    'GTQ':'Guatemalan_quetzal',
           'HKD':'Hong_Kong_dollar',     'HRK':'Croatian_kuna',                'HUF':'Hungarian_forint', 'IDR':'Indonesian_rupiah',
           'ILS':'Israeli_new_shekel',   'INR':'Indian_rupees',                'ISK':'Icelandic_krona',  'JPY':'Japanese_yen',
           'KRW':'South_Korean_won',     'KZT':'Kazakhstani_tenge',            'MXN':'Mexican_peso',     'MYR':'Malaysian_ringgit',
           'NOK':'Norwegian_krone',      'NZD':'New_Zealand_Dollar',           'PAB':'Panamanian_balboa','PEN':'Peruvian_sol',
           'PHP':'Philippine_peso',      'PKR':'Pakistani_rupees',             'PLN':'Polish_zloty',     'PYG':'Paraguayan_guarani',
           'RON':'Romanian_leu',         'RUB':'Russian_ruble',                'SAR':'Saudi_riyal',      'SEK':'Swedish_Krona',
           'SGD':'Singapore_dollar',     'THB':'Thai_baht',                    'TRY':'Turkish_lira',     'TWD':'Taiwan_New_Dollar',
           'UAH':'Ukraine_hryvnia',      'UYU':'Uruguayan_peso',               'ZAR':'South_African_rand'}

def func():
    getIndex = coun.index(cb.get())
    setIndex = coun1[getIndex]
    url = 'https://v6.exchangerate-api.com/v6/Enter_API_Key_Here/latest/{}'.format(setIndex)
    response = requests.get(url)
    data = response.json()
    
    From = cb1.get()
    to = cb.get()
    
    toCountry = content1.get()
    print(toCountry)
    getIndex = coun.index(cb1.get())
    setIndex = coun1[getIndex]
    
    fromCountry = data['rates'][setIndex]
    print(fromCountry)
    print(float(toCountry)*fromCountry)
    
    content2.set(float(toCountry)*fromCountry)

def callfunc(event):
    getIndex = coun.index(cb.get())
    setIndex = coun1[getIndex]
    getIndex = coun.index(cb1.get())
    setIndex = coun1[getIndex]
    
win =Tk()
win.geometry('580x300')
win.title('Currency Converter')
myfont = font.Font(weight="bold",size="20")
l1=Label(win,text="Currency Converter",bd='20',fg='grey')
l1['font']=myfont
l1.place(height=30,x=140,y=20)


#Combobox for fromCountry
from1 = Label(win, text="From")
myfont = font.Font(size="15")
from1['font']=myfont
from1.place(height=20,x=140,y=60)

coun = []
for i in country.values():
    coun.append(i)

coun1 = []
for i in country.keys():
    coun1.append(i)

print(coun1)
        
cb=ttk.Combobox(win,values=coun,width=30)
cb.place(height=35,x=75,y=100)
cb.current(0)
cb.bind("<<ComboboxSelected>>",callfunc)

#Combobox for toCountry
to1 = Label(win, text="To")
myfont = font.Font(size="15")
to1['font']=myfont
to1.place(height=20,x=450,y=60)


cb1=ttk.Combobox(win,values=coun,width=30)
cb1.place(height=35,x=365,y=100)
cb1.current(0)
cb1.bind("<<ComboboxSelected>>",callfunc)

#amount of currency
amount = ttk.Label(win, text="Amount")
myfont = font.Font(size="15")
amount['font']=myfont
amount.place(height=25,x=135,y=150)
content1 =StringVar()
content2 =StringVar()


e1 = ttk.Entry(win,textvariable=content1)
e1.place(height=25,x=110,y=180)

content1.set('1')
content2.set('1')
result = ttk.Label(win, text="Result")
myfont = font.Font(size="15")
result['font']=myfont
result.place(height=25,x=440,y=150)

e2 = ttk.Entry(win,state='readonly',textvariable=content2)
e2.place(height=25,x=400,y=180)


b = Button(win,text="Convert",width=20,bg='#afd6ad',command=func)
b.place(height=30,x=220,y=230)



win.mainloop()
    