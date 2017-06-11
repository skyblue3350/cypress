# cypress
ngx_http_auth_request_moduleと組み合わせて利用するLDAPのSSOシステムです．
設定例はexampleを参考にして下さい．
Python3系で動作します．

## 利用
### クイックスタート
Dockerを利用してすぐに使うことができます
```
$ git clone https://github.com/skyblue3350/cypress
$ vi docker-compose.yml
各パラメータを環境に合わせたものに変更して下さい
$ docker-compose up -d --build
```
nginx側の設定をサンプルを参考にして変更をします．

### システムにインストール
```
$ git clone https://github.com/skyblue3350/cypress
$ pip install -r requirements.txt
$ vi config.py
各パラメータを環境に合わせたものに変更して下さい
$ python app.py // or use mod_wsgi etc...
```

## 環境変数
システムに直にインストールする場合はconfig.pyを編集して下さい

| Parameter | Default |Description |
|-----------|---------|------------|
| DEBUG     | False   |Webブラウザ上でデバッグ情報を出力します|
| HOST      | 0.0.0.0 |ホスト名    |
| PORT      | 80      |ポート      |
| SECRET_KEY| abcdefg |クッキーの暗号化に利用されます　ランダムな文字列の利用を推奨します|　
| SESSION_LIFETIME | 1440 |セッションの有効時間を設定します 単位は分です|
| LDAP_HOST | 192.168.1.1 |LDAPのホスト|
| LDAP_BASE_DN | dc=example,dc=co,dc=jp |BASE DNを入力します|
| LDAP_USER_DN | ou=people |ユーザー名として利用するouを指定します|
| LDAP_USER_RDN_ATTR | uid |ユーザーIDに利用するカラム名を指定します|
| LDAP_GROUP_OBJECT_FILTER | (objectClass=posixGroup) |ユーザーが所属しているグループを指定します|


