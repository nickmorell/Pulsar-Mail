import imaplib
import email
from .mailbox import Mailbox


class IMAPHandler:

    def __init__(self, host, username, password):
        self.mail = imaplib.IMAP4_SSL(host)
        self.mail.login(username, password)
        self.mailboxes = self.refresh_mailboxes()

    def refresh_mailboxes(self):
        mailbox_list = []

        for mailbox in self.mail.list()[1]:
            parsed_mailbox = mailbox.decode().split(' "/" ')
            m = Mailbox(name=parsed_mailbox[1], child=None, no_select=('Noselect' in parsed_mailbox[0]))
            mailbox_list.append(m)

        return mailbox_list

    def refresh_mail(self, mailboxes):
        all_mail = []
        for mailbox in mailboxes:
            # Skip for now until I know how to handle it
            mailbox_name = mailbox.get_name()
            print(mailbox_name)
            if mailbox.get_no_select():
                continue
            # if mailbox_name.startswith('\"['):
            #     continue

            self.mail.select("{}".format(mailbox.get_name()))
            _, search_data = self.mail.search(None, 'ALL')
            messages = []

            for num in search_data[0].split():
                email_data = {}
                _, data = self.mail.fetch(num, '(RFC822)')
                _, b = data[0]
                email_message = email.message_from_bytes(b)

                for header in ['subject', 'to', 'from', 'date']:
                    email_data[header] = email_message[header]

                for part in email_message.walk():
                    try:
                        if part.get_content_type() == 'text/plain':
                            body = part.get_payload(decode=True)
                            email_data['body'] = body.decode()

                        if part.get_content_type() == 'text/html':
                            html_body = part.get_payload(decode=True)
                            email_data['html_body'] = html_body.decode()
                    except Exception as err:
                        print(err)
                        continue
                messages.append(email_data)
            all_mail.append({mailbox_name: messages})
        return all_mail

    def close_connection(self):
        if self.mail:
            self.mail.close()
