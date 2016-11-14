import random
from collections import namedtuple
import smtplib
from email.mime.text import MIMEText

User = namedtuple('User', ['first', 'mail'])

msg = ('Bonjour {user.first},\n'
       '\n'
       'Santa t\'a désigné pour donner un cadeau à {give_to.first} cette année.\n'
       '\n'
       'Joyeuses Paques !')

message_subject = '[SANTA] Pour la chaine de cadeaux tu devras donner le tien à ...'

smtp_server = 'smtp.jdlm.tech'
login = 'sebastien@jdlm.tech'
passwd = ''

server = smtplib.SMTP(smtp_server)
server.login(login, passwd)

def send_mail(user, give_to, msg, subject):
    msg_text = msg.format(user=user, give_to=give_to)
    msg = MIMEText(msg_text, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = user.mail
    msg['To'] = give_to.mail

    server.sendmail(user.mail, [give_to.mail], msg.as_string())

def permute(l):
    copy = list(l)
    while any(copy[i] == l[i] for i in range(len(l))):
        random.shuffle(copy)
    return copy

nb = int(input('Combien de *joueurs* ? '))
print ('')
users = []
for i in range(nb):
    print ('Joueur ' + str(i))
    first = str(input('Prénom : '))
    mail = str(input('Mail : '))
    print ('')

    users.append(User(first, mail))

deranged = permute(users)
for user,give_to in zip(users, deranged):
    send_mail(user, give_to, msg, message_subject)
