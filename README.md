# Django Heroku Template
 
## Django Heroku Deploy 参考
- [本堂俊輔さんのYoutube](https://www.youtube.com/watch?v=vV_eUbaEH2A)

## 開発時の注意点
- DEBUG=False条件でも動くか確認しながら開発する
- 使用するstaticファイルは最小限にする

## Environmental Settings
- OS: Mac Monterey 12.4
- Python: 3.7.9
- Virtual Env: venv
- Production: Heroku

## 実行
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py collectstatic
4. python manage.py runserver [port]

## 初期設定
- Herokuでアプリ作成
- Githubアカウントと連携&CI/CD設定
- .git ファイルを削除
- git init
- githubでリモートリポジトリ作成
- git remote add origin {{remote url}}
- git add .
- git commit -m 'init'
- git push origin master
- python3 -m venv ./venv --prompt {{env-name}}
- source venv/bin/activate
- python -m pip install -r requirements.txt
- /Users/naoshi/Desktop/{{app-name}}/venv/bin/python -m pip install --upgrade pip
- python manage.py collectstatic
- python manage.py migrate
- python manage.py runserver 8001

## staticファイルの追加方法
1. staticフォルダ以下に該当ファイルを設置
2. python manage.py collectstatic
3. cmd + Cでrunserverを停止&再起動
4. リロード

## static files import error
- STATIC_ROOT: 本番環境でのみ利用される。nginxで静的ファイルを配信したい場合など。manage.py collectstaticによって静的ファイルがここにコピーされる。
- STATICFILES_DIRS: ローカルで使用。cssが存在する全てのディレクトリを指定する。{% static %}タグを使った際に見に行く先のフォルダ.collectstaticを実行した際に見に行くフォルダ
- STATIC_URL: https://static.example.org/filename.extにおける、https://static.example.org 部分のURL.

## gitの運用
1. git clone
2. git branch dev
3. git checkout dev
4. 開発
5. git add, commit
6. git push origin dev
7. プルリク作成
8. マージ
9. git checkout master #masterを最新化したい
10. git pull #最新状態を取り込める

## heroku posgres連携
- heroku run python manage.py createsuperuser --app {{appname}}
- settings.pyに以下を追加すると自動でHerokuDBを読み込んでくれる
′′′
import django_heroku
django_heroku.settings(locals())
′′′

## postgres operations
- heroku addons
- heroku pg
- heroku run python manage.py migrate appName　(きちんと指定する)
- heroku run python manage.py createsuperuser
- heroku psql
- \dt; (show all tabeles)
- SELECT username, email FROM auth_user;
- \q (quit)

## maintenance
heroku maintenance:on

## database migration
- python manage.py dumpdata > dump.json (出力の全てがdump.jsonに記載されてしまうため注意。printなどで出力したものもファイルに記載されてしまう。その部分は削除してからロードする。) 
- pg_dumpall > dumpfile

## DEBUG=True時の500severerrorの対応
- htmlファイルが存在しないstaticファイルを参照しようとしている可能性がある。0からhtmlを構築した方がよい。

## Procfile for Auto Migration
- web: gunicorn myapp.wsgi
- release: python manage.py migrate
