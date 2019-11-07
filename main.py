# coding:utf-8

import os
import tkinter as tk
import tkinter.font as tkFont
import tkinter.filedialog as tkFile
import tkinter.messagebox
from PIL import ImageTk
import tkutils as tku
import split_file as splitFile

class App:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("%dx%d" % (700, 400))   # 窗体尺寸
		tku.center_window(self.root)               # 将窗体移动到屏幕中央
		self.root.iconbitmap("images\\title.ico")  # 窗体图标
		self.root.title("Python 分割文件")
		self.root.resizable(False, False)          # 设置窗体不可改变大小
		self.file_path = ''          			   # 设置要要分割的文件为
		self.file_num = 5          			   	   # 设置要要分割的文件为 None
		self.save_path = ''          			   # 设置要要分割后保存的文件夹
		self.font_one = tkFont.Font(family="微软雅黑", size=14, weight=tkFont.BOLD)
		self.font_two = tkFont.Font(family="微软雅黑", size=14, weight=tkFont.BOLD)
		self.no_title = True
		self.body()

	def body(self):
		# ---------------------------------------------------------------------
		# 背景图片
		# ---------------------------------------------------------------------
		self.img = ImageTk.PhotoImage(file="images\\bg.png")
		canvas = tk.Canvas(self.root, width=720, height=420)
		self.canvas = canvas
		canvas.create_image(300, 200, image=self.img)
		canvas.pack(expand=tk.Y, fill=tk.BOTH)

		# ---------------------------------------------------------------------
		# 功能按钮组
		# ---------------------------------------------------------------------
		tk.Button(self.canvas, text="选择文件", bg="cadetblue", command=self.get_file_path, font=self.font_two, height=1, fg="white", width=10)\
			.place(x=20, y=20)
		tk.Button(self.canvas, text="保存路径", bg="cadetblue", command=self.get_save_dir, font=self.font_two, height=1,
				  fg="white", width=10) \
			.place(x=20, y=100)
		tk.Button(self.canvas, text="文件数量", bg="cadetblue", command=self.fill_file_num, font=self.font_two, height=1, fg="white", width=10)\
			.place(x=20, y=180)
		tk.Button(self.canvas, text="开始分割", bg="green", command=self.split_file, font=self.font_two, height=1, fg="white", width=10)\
			.pack(side=tk.BOTTOM, expand=tk.NO, anchor=tk.SE, padx=50, pady=30)

	def get_file_path(self):
		self.file_path = tkFile.askopenfilename()
		tk.Label(self.canvas, text=self.file_path, height=1, fg="white", font=self.font_one, bg="Teal")\
		.place(x=200, y=26)

	def get_save_dir(self):
		self.save_path = tkFile.askdirectory()
		tk.Label(self.canvas, text=self.save_path, height=1, fg="white", font=self.font_one, bg="Teal")\
		.place(x=200, y=106)

	def fill_file_num(self):
		def get_value():
			self.file_num = entry_new_name.get()
			tmp_window.destroy()
			tk.Label(self.canvas, text=self.file_num, height=1, fg="white", font=self.font_one, bg="Teal") \
				.place(x=200, y=188)

		tmp_window = tk.Toplevel(self.root)			# 创建新的窗口
		tmp_window.geometry('200x100')				# 设置新窗口大小
		tmp_window.title('文件数量')					# 设置新窗口标题
		tku.center_window(tmp_window)				# 设置新窗口位置
		tmp_window.resizable(False, False)			# 禁止修改新窗口大小
		new_name = tk.StringVar()					# 创建新的输入框
		new_name.set('5')							# 默认值为 5
		entry_new_name = tk.Entry(tmp_window, textvariable=new_name)		# 设置
		entry_new_name.pack(side=tk.TOP, expand=tk.YES,anchor=tk.CENTER)
		tmp_font = tkFont.Font(family="微软雅黑", size=10)
		tk.Button(tmp_window, text="确定", bg="green", command=get_value, font=tmp_font, fg="white",
				  width=5) \
			.pack(side=tk.BOTTOM, expand=tk.NO, anchor=tk.CENTER, padx=5, pady=5)

	def split_file(self):
		if os.path.exists(self.file_path) is False:
			tk.messagebox.showerror(title='错误', message="文件不存在！")
			return
		elif os.path.exists(self.save_path) is False:
			tk.messagebox.showerror(title='错误', message="保存路径不存在！")
			return
		elif int(self.file_num) < 1 :
			tk.messagebox.showerror(title="错误", message="文件数量错误")
			return
		tk.messagebox.showinfo(title="提示", message="分割文件中.....")
		res = splitFile.split_file(self.file_path,int(self.file_num),self.save_path)
		if res:
			tk.messagebox.showinfo(title="提示", message="分割完成")
		else:
			tk.messagebox.showerror(title="错误", message="分割出错")




if __name__ == "__main__":
	app = App()
	app.root.mainloop()
