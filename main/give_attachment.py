from Class_Mailbox import MailBox
from config import accaunt_login, accaunt_password
import time
import schedule
from schedule import every, repeat


@repeat(every(10).seconds)
def get_attachment():
    with MailBox(accaunt_login, accaunt_password) as attach:
        list_filenames = attach.get_attachment_from_unread()
        return list_filenames


while True:
    schedule.run_pending()
    time.sleep(1)
