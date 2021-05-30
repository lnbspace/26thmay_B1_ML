import tkinter as tk
app = tk.Tk()
app.title('Registration Form')
app.geometry('400x280')
#

f_name = tk.Variable(app)
e_mail = tk.Variable(app)
u_name = tk.Variable(app)
pwd = tk.Variable(app)
age = tk.Variable(app)
mobile = tk.Variable(app)

tk.Label(app, text='Full Name').place(x=20,y=30)
tk.Label(app, text='Email ID').place(x=20,y=60)
tk.Label(app, text='User Name').place(x=20,y=90)
tk.Label(app, text='Password').place(x=20,y=120)
tk.Label(app, text='Age').place(x=20,y=150)
tk.Label(app, text='Mobile').place(x=20,y=180)

tk.Entry(app,width=30,bg='#ffffff', textvariable=f_name).place(x=150,y=30)
tk.Entry(app,width=30,bg='#ffffff', textvariable=e_mail).place(x=150,y=60)
tk.Entry(app,width=30,bg='#ffffff', textvariable=u_name).place(x=150,y=90)
tk.Entry(app,width=30,bg='#ffffff', textvariable=pwd).place(x=150,y=120)
tk.Entry(app,width=30,bg='#ffffff', textvariable=age).place(x=150,y=150)
tk.Entry(app,width=30,bg='#ffffff', textvariable=mobile).place(x=150,y=180)

def register():
    
    f = open('data.csv','a')
    data = [f_name.get(),e_mail.get(),u_name.get(),pwd.get(),age.get(),mobile.get()]
    f.write(','.join(data)+'\n')

    f.close()
    f_name.set('')
    e_mail.set('')
    u_name.set('')
    pwd.set('')
    age.set('')
    mobile.set('')

tk.Button(app, text='Submit', command=register).place(x=150,y=210)

#
app.mainloop()
