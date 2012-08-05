import speech
# import time

from src.mail import mail

master='Marra'

if __name__ == '__main__':
    # m = mail(name='AOL Mail', server='imap.aol.com', username='llagerman@aol.com', password='travis')
    m = mail(name='AOL Mail', server='imap.aol.com', username='kanewna@aol.com', password='27uW4dMZ7Vj2^t%c')
    # speech.say("Hello "+master+" what would you like to do?")
    for folderName in m.folders:
        print folderName
    m.select_folder("INBOX")
    print m.UnreadCount
    
    m.logout()