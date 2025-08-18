from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

window = Tk()
window.title("WaterMark Adder")
window.config(padx=20, pady=20)

img = None
tk_image = None
image_label = None
last_watermarked = None


def add_watermark():
    global img, tk_image, image_label, last_watermarked
    if img:
        watermark_input = input_entry.get()
        last_watermarked = img.copy()
        draw = ImageDraw.Draw(last_watermarked)

        width, height = last_watermarked.size
        font_size = max(15, width // 15)
        font = ImageFont.truetype("arial.ttf", font_size)

        bbox = draw.textbbox((0, 0), watermark_input, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = width - text_width - 10
        y = height - text_height - 10

        draw.text((x, y), watermark_input, font=font, fill=(255, 255, 255))

        tk_image = ImageTk.PhotoImage(last_watermarked)
        image_label.config(image=tk_image)
        image_label.image = tk_image


def choose_file():
    global img, tk_image, image_label

    file_path = filedialog.askopenfilename(
        title="Select the image you want to add the watermark to",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if file_path:
        img = Image.open(file_path)
        max_size = (300, 300)
        img.thumbnail(max_size)

        tk_image = ImageTk.PhotoImage(img)

        if image_label is None:
            image_label = Label(window, image=tk_image)
            image_label.grid(column=2, row=1)
        else:
            image_label.config(image=tk_image)
        image_label.image = tk_image


def save_watermark():
    global last_watermarked
    if last_watermarked:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"),
                       ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if file_path:
            last_watermarked.save(file_path)


add_file = Button(text="Choose Image", command=choose_file)
add_file.grid(column=1, row=2)

watermark_text = Label(text="Add watermark text here")
watermark_text.grid(column=0, row=0)

input_entry = Entry(width=20)
input_entry.grid(column=1, row=0)

add_button = Button(text="Add watermark", command=add_watermark)
add_button.grid(column=2, row=0)

save_button = Button(text="Save Image", command=save_watermark)
save_button.grid(column=2, row=2)

window.mainloop()
