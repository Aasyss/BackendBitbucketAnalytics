#!/bin/bash
cd /home/provii/Desktop/bitbucketanalysis/
source venv/bin/activate
python manage.py update_commit
python manage.py update_files


