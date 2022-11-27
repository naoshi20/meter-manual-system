# Meter Manual System

## cautions

- DEBUG=False 条件でも動くか確認しながら開発する
- 使用する static ファイルは最小限にする

## environment

- OS: Mac Monterey 12.4
- Python: 3.7.9
- Virtual Env: venv
- Production: Heroku

## initial settings

- Heroku でアプリ作成
- Github アカウントと連携&CI/CD 設定
- .git ファイルを削除
- git init
- github でリモートリポジトリ作成
- git remote add origin {{remote url}}
- git add .
- git commit -m 'init'
- git push origin master
- python3 -m venv ./venv --prompt {{env-name}}
- source venv/bin/activate
- python -m pip install -r requirements.txt
- /Users/naoshi/Desktop/{{app-name}}/venv/bin/python -m pip install --upgrade pip
- .env ファイルをルートに作成し、下記を追加。
  ’’’SECRET_KEY=^(%2r5@=actnpa%gppjp&ur-=goad=dar(=0#n-^x4lby$353g
  DEBUG=True’’’
- python manage.py collectstatic
- python manage.py migrate
- python manage.py runserver 8001

## execution

1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py collectstatic
4. python manage.py runserver [port]

## add static file

1. static フォルダ以下に該当ファイルを設置
2. python manage.py collectstatic
3. cmd + C で runserver を停止&再起動
4. reload browser

## static files import error

- STATIC_ROOT: 本番環境でのみ利用される。nginx で静的ファイルを配信したい場合など。manage.py collectstatic によって静的ファイルがここにコピーされる。
- STATICFILES_DIRS: ローカルで使用。css が存在する全てのディレクトリを指定する。{% static %}タグを使った際に見に行く先のフォルダ.collectstatic を実行した際に見に行くフォルダ
- STATIC_URL: https://static.example.org/filename.extにおける、https://static.example.org 部分の URL.

## for heroku posgres integration

- heroku run python manage.py createsuperuser --app {{appname}}
- settings.py に以下を追加すると自動で HerokuDB を読み込んでくれる
  ′′′
  import django_heroku
  django_heroku.settings(locals())
  ′′′

## postgres operations

- heroku addons
- heroku pg
- heroku run python manage.py migrate appName 　(きちんと指定する)
- heroku run python manage.py createsuperuser
- heroku psql
- \dt; (show all tabeles)
- SELECT username, email FROM auth_user;
- \q (quit)

## maintenance mode

heroku maintenance:on

## database migration

- python manage.py dumpdata > dump.json
- pg_dumpall > dumpfile

## solution for 500 sever error

- html ファイルが存在しない static ファイルを参照しようとしている可能性がある。0 から html を構築した方がよい。

## Procfile for Auto Migration

- web: gunicorn myapp.wsgi
- release: python manage.py migrate
