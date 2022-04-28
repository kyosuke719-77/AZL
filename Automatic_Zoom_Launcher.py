import tkinter
from tkinter import ttk
from tkinter import messagebox

#テキストボックスの値を抽出
def val_get():
    url=url_box.get()
    met_id=id_box.get()
    met_pwd=pwd_box.get()
    class_name=class_box.get()
    judge(url, met_id, met_pwd, class_name)

#処理分岐用関数
def judge(url, met_id, met_pw, class_name):
    if(class_name == ''):
        error(0)
    elif(url != '' or (met_id != '' and met_pw != '')):
        if(url != ''):
            if(met_pw != ''):
                marge(url, met_pw, class_name)
            else:
                id_export(url,class_name)
        else:
            create_bat(met_id, met_pw, class_name)
    else:
        error(2)

#確認ウィンドウの表示
def confirm():
    messagebox.showinfo("登録確認","接続情報を登録しました")
    main_win.destroy()

#エラーメッセージの表示
def error(flag):
    if(flag==0):
        messagebox.showerror('エラー', '授業名が登録されていません')
    elif(flag==1):
        messagebox.showerror('エラー', 'URLにID若しくは、パスワードが含まれていません')
    else:
        messagebox.showerror('エラー', '登録すべき情報に不足があります')

#PWなしURLとPWの組からbatファイルを作成するための処理
def marge(url,met_pw,class_name):
    pwd_target=url.find('?pwd')
    if(pwd_target < 0):
        url=url+'pwd='+met_pw
    id_export(url,class_name)

#URLからidとpwを抽出
def id_export(url, class_name):
    id_target=url.find('/j/')
    pwd_target=url.find('?pwd')
    if(id_target<0 or pwd_target<0):
        error(1)
    else:
        met_id=url[id_target+3:pwd_target]
        met_pwd=url[pwd_target+5:]
        create_bat(met_id, met_pwd, class_name)

#batファイルの作成
def create_bat(met_id, met_pwd, class_name):
    met_id=met_id.replace(' ','')
    with open('./' + class_name + '.bat', 'w', encoding='utf-8')as file:
        file.write('@echo off\n')
        file.write('start zoommtg:\"//zoom.us/join?action=join&confno=' + met_id + '&pwd=' + met_pwd + '\"')
    file.close()
    confirm()

#以下メインのGUIループ処理

main_win=tkinter.Tk()
main_win.attributes("-topmost", True)
main_win.title("Automatic Zoom Launcher")
main_win.geometry("600x180")

main_frm=ttk.Frame(main_win)
main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

#URL
url_label=ttk.Label(main_frm, text="接続URL")
url_box=ttk.Entry(main_frm)

#ID, PW, class
id_label=ttk.Label(main_frm, text="接続ID")
id_box=ttk.Entry(main_frm)
pwd_label=ttk.Label(main_frm, text="passward")
pwd_box=ttk.Entry(main_frm)
class_label=ttk.Label(main_frm, text="授業名")
class_box=ttk.Entry(main_frm)

#登録ボタン
app_btn=ttk.Button(main_frm, text='登録', command=val_get)

url_label.grid(column=0, row=0, pady=10)
url_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
id_label.grid(column=0, row=1)
id_box.grid(column=1, row=1, sticky=tkinter.W, padx=5)
pwd_label.grid(column=0, row=2)
pwd_box.grid(column=1, row=2, sticky=tkinter.W, padx=5)
class_label.grid(column=0, row=3, pady=10)
class_box.grid(column=1, row=3, sticky=tkinter.W, padx=5)
app_btn.grid(column=1, row=4)

main_win.columnconfigure(0, weight=1)
main_win.rowconfigure(0, weight=1)
main_frm.columnconfigure(1, weight=1)

main_win.mainloop()


