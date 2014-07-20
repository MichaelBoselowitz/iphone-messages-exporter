import sqlite3
import os
from datetime import datetime

# Where to place the backup directories
BACKUP_PATH = './backup'
# Path for iPhone backups
PHONE_BACKUP_PATH = os.path.expanduser('~/Library/Application Support/MobileSync/Backup')

os.mkdir(BACKUP_PATH)

backups = [os.path.join(PHONE_BACKUP_PATH, x) for x in os.listdir(PHONE_BACKUP_PATH) if os.path.isdir(os.path.join(PHONE_BACKUP_PATH, x))]

most_recent_backup = False
for backup in backups:
    if not most_recent_backup or os.path.getctime(most_recent_backup) < os.path.getctime(backup):
        most_recent_backup = backup
most_recent_backup = os.path.join(most_recent_backup, '3d0d7e5fb2ce288813306e4d4636395e047a3d28')

db = sqlite3.connect(most_recent_backup)
handles = db.execute('select * from handle')

for handle in handles:
    messages = db.execute('select is_from_me,date,text from message where handle_id=%s' % (handle[0]))

    try:
        os.mkdir(os.path.join(BACKUP_PATH, handle[1]))
    except OSError:
        pass

    fp = open(os.path.join(BACKUP_PATH, handle[1], 'log.txt'), 'a')
    for message in messages:
        who = 'me' if message[0] == 1 else handle[1]
        # iMessages bases it's dates from Jan 1, 2001
        date = datetime.fromtimestamp(message[1] + 978307200)
        out_message = ('%s - %s: %s' % (date, who, message[2])).encode('utf-8')
        fp.write('%s\n' % (out_message))
    fp.close()
