#!/usr/bin/python
# -*- coding: utf8 -*-

import smtplib

"""
Scripts of the checking mail behavior
"""

class MailMonitor(object):
    def __init__(self):
        pass

    def sendMessage(self, mail):
        # From addr
	fromaddr = mail['from']

	# To addr
	to_main_addr = mail['to_main']
	to_back1_addr = mail['to_back1']
	to_back2_addr = mail['to_back2']
	to_back_addr = mail['to_back1'],mail['to_back2']
	# Bcc addr
	bcc_addr = mail['bcc']

	# Subject
	subject1 = mail['subject1']
	subject2 = mail['subject2']

	# message
	msg_main = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (fromaddr, to_main_addr, subject1))
	msg_back = ("From: %s\r\nTo: %s, %s, %s\r\nBCC: %s\r\nSubject: %s\r\n\r\n" % (fromaddr, to_back1_addr, to_back2_addr, bcc_addr, subject2))

	line_main = mail['msg_main']
	line_back = mail['msg_back']

	msg_main = msg_main + line_main
	msg_back = msg_back + line_back

	try:
	    server = smtplib.SMTP(host='192.168.1.52', port=25, timeout=30)
	    server.set_debuglevel(1)
	    server.sendmail(fromaddr, to_main_addr, msg_main)
	    server.quit()
	except Exception:
	    server = smtplib.SMTP('192.168.1.52', 25)
	    server.set_debuglevel(1)
	    server.sendmail(fromaddr, to_back_addr, msg_back)
	    server.quit()

def main():
    # Defined the mail address
    mail = {
        'from': 'from-address@example.com',
	'to_main': 'to-mail-address@example.com',
	'to_back1': 'to-back1-address@example.com',
	'to_back2': 'to-back2-address@example.com',
	'bcc': 'bcc-address@example.com',
	'subject1': 'normal',
	'subject2': 'abnormal',
	'msg_main': 'this is a normal message',
	'msg_back': 'this is a abnormal message',
    }

    mm = MailMonitor()
    mm.sendMessage(mail)


if __name__ == '__main__':
    main()
