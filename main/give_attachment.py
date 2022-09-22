from Class_Mailbox import MailBox
from config import accaunt_login, accaunt_password
import time
import schedule
from schedule import every, repeat


@repeat(every(360).seconds)
def get_attachment():
    with MailBox(accaunt_login, accaunt_password) as attach:
        attach.get_attachment_from_unread()


while True:
    schedule.run_pending()
    time.sleep(1)
