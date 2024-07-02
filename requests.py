import os
import pysftp #install bcrypt(3.2.0) + paramiko(3.4.0) + cryptography

USERNAME = USERNAME
PASSWORD = PASSWORD
IP = IP
PORT = PORT

try:
    user = USERNAME
    password = PASSWORD
    ip = IP
    port = PORT
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    name = datetime.today().strftime('%d-%m-%Y')
    
    with pysftp.Connection(host=ip, username=user, password=password, cnopts=cnopts, port=port) as sftp:
        print("Connection established")
        
        try:
            os.mkdir(name)
            print(f"Directory '{name}' created.")
        except FileExistsError:
            print(f"Directory '{name}' already exists.")
        
        remote_dir = "./Desktop/{}".format(name)
        local_dir = "./result/{}".format(name)
        
        try:
            sftp.get_d(remotedir=remote_dir, localdir=local_dir)
            print(f"Downloaded files from {remote_dir} to {local_dir}")
        except Exception as e:
            print(f"Error downloading files: {e}")

except Exception as e:
    print(f"Error: {e}")
