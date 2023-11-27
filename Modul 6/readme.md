# Persiapan

1. kamu harus menginstall libffi terlebih dahulu sebelum menginstall modul fabric dengan mengeksekusi perintah berikut
```bash
sudo apt-get install libffi-dev
```
2. dan kamu harus menginstall modul setuptools-rust dengan perintah berikut
Python 2.x
```bash
pip2 install setuptools-rust
```
Python 3.x
```bash
pip3 install setuptools-rust
```
# Cara Run 6.5

```bash
ln -sfn 6_5_run_mysql_command_remotely.py fabfile.py
fab remote_server show_dbs
```

jika belum terinstall fabric
```bash
pip install fabric
```
```bash
sudo apt install fabric
```

# Cara Run 6.6

```bash
ln -sfn 6_6_new_transfer_file_over_ssh.py fabfile.py
fab remote_server login
```
