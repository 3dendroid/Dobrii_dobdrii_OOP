import sys

class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = bool(fl_read)

    def __bool__(self):
        return self.is_read


class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        for line in lst_in:
            # разбиваем по первому двум точкам с запятой
            parts = [p.strip() for p in line.split(';', 2)]
            mail_from, title, content = parts
            item = MailItem(mail_from, title, content)
            self.inbox_list.append(item)


# --- основная часть программы ---
mail = MailBox()
mail.receive()

# отмечаем первое и последнее письмо как прочитанное
if mail.inbox_list:
    mail.inbox_list[0].set_read(True)
    mail.inbox_list[-1].set_read(True)

# формируем отфильтрованный список прочитанных писем
inbox_list_filtered = list(filter(bool, mail.inbox_list))
