from tkinter import messagebox
from PIL import ImageTk
from xes.uploader import *
from tkinter import *
from PIL import Image as imim
from tkinter.filedialog import *
import tkinter.ttk as ttk
import threading
import tkinter as tk
import webbrowser as web


def message(title, msg):
    messagebox.showinfo(title, msg)
def start_window():
    # 创建一个Tkinter窗口
    start = tk.Tk()
    #不显示Windows原生标题栏
    start.overrideredirect(True)

    # 关闭窗口的函数
    def close_window():
        start.destroy()

    # 加载并显示图像
    image = imim.open('start.png')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(start, image=photo)
    label.pack()

    # 浅浅设置窗口的尺寸和位置（在屏幕中居中显示）
    width, height = image.size
    screen_width = start.winfo_screenwidth()
    screen_height = start.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    start.geometry(f"{width}x{height}+{x}+{y}")

    # 在1000毫秒（1秒）后关闭窗口，此处为调用close_window的函数
    start.after(1000, close_window)

    # 启动Tkinter的主循环
    start.mainloop()

def about_window():
    about_new_window = Tk()
    about_new_window.title('关于')

    # 设置窗口图标
    about_new_window.iconbitmap('xes.ico')

    # 加载并显示图像
    about_new_logo = PhotoImage(file='logo.png')
    logo_about = tk.Label(about_new_window, image=about_new_logo)
    logo_about.pack()

    # 显示版本号文字
    v_text = "V2.0.0"
    text_label = tk.Label(about_new_window, text=v_text, font=('黑体', 17), fg='#8EC0F9')
    text_label.pack()

    # 显示关于信息文字
    about_text = "Rabbit Studio\n作者：Rabbit max\n\n访问：\nhttps://cncyx.cn\nhttps://irabbitmax.site"
    about_new_text = tk.Label(about_new_window, text=about_text, wraplength=300, justify='center', font=('黑体', 13))
    about_new_text.pack(pady=5)

    about_new_window.mainloop()
def pan_main():
    path = ""
    ss = ""
    #初始化 兔兔加油呀
    home = Tk()
    home.title("学而思网盘-V2.0")
    home.geometry("500x300")
    home.iconbitmap('xes.ico')
    home.resizable(0, 0)

    #导航栏 awa
    n = ttk.Notebook(home)

    up = Frame(home)
    down = Frame(home)
    setting = Frame(home)

    def pan_exit():
        home.destroy()

    def choose_file():
        try:
            global path
            a = askopenfilename(title="学而思网盘-请选择您需要上传的文件")
            if a == "" or a == None:
                return
            path = a
            tg.delete('1.0', 'end')
            tg.insert(END, f"文件路径：{path}")
            sta.config(text="选择成功，路径👇", fg="black")
        except:
            pass


    def up_file():
        try:
            global path
            if path == "":
                sta.config(text="您还未选择文件，请选择文件后重试！", fg="red")
                return
            sta.config(text="正在上传（请不要执行其他上传操作）")
            true_file = xp.uploadAbsolutePath(path)
            tg.delete('1.0', 'end')
            tg.insert(END,
                      "【Rabbit Studio】学而思网盘 上传成功，链接：\n" + true_file + f"\n\n选中后Ctrl+C可复制！\n提示：直链下载，可直接复制到浏览器！\n\n")
            sta.config(text="上传完成")
        except:
            pass

    def uptarget():
        try:
            global ss
            ss = threading.Thread(target=up_file)
            ss.start()
        except:
            pass

    def down_file():
        web.open(downhttp)

    def update_message():
        message("提示","检测更新功能还未制作")
    #上传
    gd = Frame(up)
    gd.pack(expand=1)
    logo_img_png = PhotoImage(file='logo.png')
    logo_img = Label(gd, image=logo_img_png)
    logo_img.grid(row=0, column=1)

    up_img = PhotoImage(file='upload.png')
    ttk.Button(gd, text="选择", command=choose_file).grid(row=1, column=0)
    ttk.Button(gd, image=up_img, command=uptarget).grid(row=1, column=2)

    sta = Label(up, text="您还未选择文件")
    sta.pack()
    tg = Text(up)
    tg.pack(expand=1)

    #下载
    down_window = Frame(down)
    down_window.pack()
    Label(down_window, text="下载文件", justify='center',font=("黑体", 20)).grid(row=0, column=2,padx=40)
    Label(down_window, text="输入下载链接：", font=("黑体", 12)).grid(row=3, column=1,padx=20)
    down_website = ttk.Entry(down_window, width=30)
    down_website.grid(row=3, column=2,padx=1,pady=50,ipady=3)
    down_img = PhotoImage(file='download.png')
    downhttp = down_website.get()
    ttk.Button(down_window, image=down_img, command=down_file).grid(row=6, column=4,padx=10,pady=60)


    #关于
    set = Frame(setting)
    set.pack()
    logo = PhotoImage(file='logo.png')
    logo_label = tk.Label(set, image=logo)
    logo_label.pack()

    # 显示文字
    about_text = "V2.0.0"
    text_label1 = tk.Label(set, text=about_text, font=('黑体', 17), fg='#8EC0F9')
    text_label1.pack()
    update_button = ttk.Button(set,text="检测更新",command=update_message)
    update_button.pack()
    ttk.Label(set).pack()
    ttk.Label(set).pack()
    ttk.Label(set).pack()
    about_button= ttk.Button(set,text="关于",command=about_window)
    about_button.pack()
    ttk.Label(set).pack()
    pan_exit_button = ttk.Button(set, text="退出",command=pan_exit)
    pan_exit_button.pack()
    '''
    text_label2 = tk.Label(about,text="Rabbit Studio\n作者：Rabbit max\n\n访问：\nhttps://cncyx.cn\nhttps://irabbitmax.site",wraplength=300, justify='center', font=('黑体', 13))
    text_label2.pack(pady=5)
    '''

    n.add(up, text="上传")
    n.add(down, text="下载")
    n.add(setting, text="设置")
    n.pack(fill=BOTH, expand=1)

    xp = XesUploader()
    home.mainloop()


if __name__ == '__main__':
    start_window()
    pan_main()
else:
    message("学而思网盘-提示","您使用的学而思网盘并非正版，可能会有风险（请勿从其它方式调用，请双击文件或快捷方式以打开，否则会提示本弹窗！）")