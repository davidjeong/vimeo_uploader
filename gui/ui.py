from tkinter import Tk, Label, Menu, StringVar, Entry, messagebox, LEFT, W, filedialog, Button

from driver.driver import get_vimeo_configuration, Driver, get_seconds
from driver.video_configuration import VideoConfiguration

root = Tk()

root.title("Vimeo Uploader")
root.geometry('640x480')

vimeo_config = None
thumbnail_path = None
url_prefix = 'https://www.youtube.com/watch?v='


def about():
    messagebox.showinfo('About', 'This is a python-based application to download youtube videos, trim them, '
                                 'and re-upload to Vimeo.')


def import_config_json():
    global vimeo_config
    filename = filedialog.askopenfilename(title='Select config file', filetypes=[('json files', '*.json')])
    vimeo_config = get_vimeo_configuration(filename)


def get_thumbnail():
    global thumbnail_path
    thumbnail_path = filedialog.askopenfilename(title='Select image file',
                                                filetypes=[('jpeg files', '*.jpg'), ('png files', '*.png')])
    image_text.set('Thumbnail path: ' + thumbnail_path)


def process_video():
    process_button['state'] = 'disabled'
    process_button['text'] = 'Processing...'

    driver = Driver(vimeo_config=vimeo_config)
    # video_url, start_time_in_sec, end_time_in_sec, resolution, video_title=None, image_url=None

    video_config = VideoConfiguration(url_prefix + url.get(), get_seconds(start_time.get()), get_seconds(end_time.get()), resolution.get(), title.get(),
                                      thumbnail_path)
    driver.process(video_config)
    process_button['state'] = 'enabled'
    process_button['text'] = 'Processing successful!'


menubar = Menu(root, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
file = Menu(menubar, tearoff=1)
file.add_command(label='About', command=about)
file.add_command(label='Import config', command=import_config_json)
file.add_command(label='Quit', command=root.quit)
menubar.add_cascade(label='File', menu=file)

root.config(menu=menubar)

url = StringVar()
start_time = StringVar()
end_time = StringVar()
image_text = StringVar()
image_text.set("Path to thumbnail image (optional)")
resolution = StringVar()
title = StringVar()

url_label = Label(root, text='Supplied link: ' + url_prefix, font=('Helvetica', 10), justify=LEFT)
url_entry = Entry(root, textvariable=url, font=('Helvetica', 10), width=15, justify=LEFT)
start_label = Label(root, text='Start time of video in format 00:00:00', font=('Helvetica', 10), justify=LEFT)
start_entry = Entry(root, textvariable=start_time, font=('Helvetica', 10), justify=LEFT, width=10)
end_label = Label(root, text='End time of video in format 00:00:00', font=('Helvetica', 10), justify=LEFT)
end_entry = Entry(root, textvariable=end_time, font=('Helvetica', 10), width=10, justify=LEFT)
image_label = Label(root, textvariable=image_text, font=('Helvetica', 10), justify=LEFT)
image_button = Button(root, text='Click to set', font=('Helvetica', 10), command=get_thumbnail, justify=LEFT)
resolution_label = Label(root, text='Video resolution (e.g. 1080p)', font=('Helvetica', 10), justify=LEFT)
resolution_entry = Entry(root, textvariable=resolution, font=('Helvetica', 10), width=10, justify=LEFT)
title_label = Label(root, text="Title of the video", font=('Helvetica', 10), justify=LEFT)
title_entry = Entry(root, textvariable=title, font=('Helvetica', 10), width=20, justify=LEFT)

process_button = Button(root, text='Start processing', font=('Helvetica', 10, 'bold'), command=process_video,
                        justify=LEFT)

url_label.grid(sticky=W, row=1, column=0)
url_entry.grid(sticky=W, row=1, column=1)
start_label.grid(sticky=W, row=2, column=0)
start_entry.grid(sticky=W, row=2, column=1)
end_label.grid(sticky=W, row=3, column=0)
end_entry.grid(sticky=W, row=3, column=1)
image_label.grid(sticky=W, row=4, column=0)
image_button.grid(sticky=W, row=4, column=1)
resolution_label.grid(sticky=W, row=5, column=0)
resolution_entry.grid(sticky=W, row=5, column=1)
title_label.grid(sticky=W, row=6, column=0)
title_entry.grid(sticky=W, row=6, column=1)
process_button.grid(sticky=W, row=7, column=1)

root.mainloop()
