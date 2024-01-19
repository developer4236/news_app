import requests 
import io
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
import webbrowser



class NewsApp:
    def __init__(self):
        
        #fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=152a3504b3874af08a32592a058407b1').json()
        
        #initilal GUI load
        self.load_gui()
        
        #load the 1st new item
        self.load_news_item(1)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('600x600')
        self.root.resizable(0,0)
        self.root.title('Newsapp')
        self.root.configure(background='black')
    
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy() 

    def load_news_item(self,index):

        #clear the screen for the new news item
        self.clear()

        #image 
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://images.wondershare.com/repairit/aticle/2021/07/resolve-images-not-showing-problem-1.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root,image=photo)
        label.pack()

    
        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='#FFA500',wraplength=600)
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',17))

        deatils = Label(self.root,text=self.data['articles'][index]['description'],bg='black',fg='white',wraplength=600)
        deatils.pack(pady=(10,20))
        deatils.config(font=('verdana',12))
    
        frame = Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

        if index != 0 :
            prev = Button(frame,text='Prev',width=27,height=3,fg='#0000FF',bg='#999999',command=lambda : self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read = Button(frame,text='ReadMore',width=28,height=3,fg='red',bg='#999999',command=lambda : self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles'])-1 :
            next = Button(frame,text='Next',width=27,height=3,fg='#0000FF',bg='#999999',command=lambda : self.load_news_item(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)

obj = NewsApp() 

        