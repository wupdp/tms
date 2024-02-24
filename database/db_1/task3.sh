#!/bin/bash

DB_USER="admin"
DB_PASS="passwd"
DB_NAME="Courses_db"

REMOTE_USER="wupdp"
REMOTE_HOST="192.168.109.203"
REMOTE_PATH="/tmp/backup"

BACKUP_FILE="/tmp/backup_$(date +'%Y%m%d_%H%M%S').sql"
mysqldump -u $DB_USER -p $DB_PASS $DB_NAME > $BACKUP_FILE

rsync -avz -e ssh $BACKUP_FILE $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH

rm $BACKUP_FILE
