from Class_Mailbox import MailBox
from config import accaunt_login, accaunt_password
from schedule import every, repeat
from bot import T_Bot


@repeat(every(60).seconds)
def get_attach():
    with MailBox(accaunt_login, accaunt_password) as attach:
        list_files = attach.get_attachment_from_unread()
        for file in list_files:
            T_Bot().send_file(file)
