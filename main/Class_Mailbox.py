import email
import imaplib
import os
from config import imap_serv
from email.header import decode_header


class MailBox:
    filenames = []

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.imap = imaplib.IMAP4_SSL(imap_serv)

    def __enter__(self):
        self.imap.login(self.user, self.password)
        return self

    def __exit__(self, tipe, value, traceback):
        self.imap.close()
        self.imap.logout()

    def get_email_message(self):
        self.imap.list()
        self.imap.select('Inbox')
        types, data = self.imap.uid('search', None, "UNSEEN")

        for x in range(len(data[0].split())):
            type_email, email_data = self.imap.uid('fetch', data[0].split()[x], '(RFC822)')
            raw_email_string = email_data[0][1].decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            return email_message

    def get_attachment_from_unread(self):
        self.imap.list()
        self.imap.select('Inbox')
        types, data = self.imap.uid('search', None, "UNSEEN")

        for x in range(len(data[0].split())):
            type_email, email_data = self.imap.uid('fetch', data[0].split()[x], '(RFC822)')
            raw_email_string = email_data[0][1].decode('utf-8')
            email_message = email.message_from_string(raw_email_string)

            for part in email_message.walk():
                if part.get_content_maintype() == "multipart":
                    continue

                if part.get('Content-Disposition') is None:
                    continue

                if part.get('Content-Type') != 'application/pdf':
                    continue

                else:
                    filename = part.get_filename()
                    if decode_header(filename)[0][1] is not None:
                        filename = decode_header(filename)[0][0].decode(decode_header(filename)[0][1])
                    if bool(filename):
                        filepath = os.path.join(filename)
                        if not os.path.isfile(filepath):
                            fp = open(filepath, 'wb')
                            fp.write(part.get_payload(decode=True))
                            self.filenames.append(filepath)
        return self.filenames

