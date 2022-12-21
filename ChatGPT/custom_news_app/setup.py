#!/usr/bin/env python

import subprocess

dependencies = ['google-api-python-client', 'requests', 'beautifulsoup4', 'openai', 'keras', 'pandas', 'sqlite3', 'click']

for dependency in dependencies:
  subprocess.run(['pip', 'install', dependency])

# create database and tables
conn = sqlite3.connect('news.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS articles (url TEXT PRIMARY KEY, summary TEXT, label INTEGER)')
conn.commit()
conn.close()

print('Dependencies and database setup complete!')
