from qbittorrent import Client
from dotenv import load_dotenv
import time
import os

load_dotenv()

while True:
    print("Checking if qBittorrent is connectable...")
    try:
        qb = Client(os.getenv('QB_URL'))
        qb.login(os.getenv('QB_USER'), os.getenv('QB_PASS'))
        connection_status = qb.global_transfer_info['connection_status']
        port = qb.preferences()['listen_port']

        if connection_status == 'connected':
            print("qBittorrent is connectable!")
        else:
            print("qBittorrent is not connectable. Changing port...")

            qb.set_preferences(listen_port=50000)
            time.sleep(5)
            qb.set_preferences(listen_port=port)

            print("Port changed successfully!")

    except Exception as e:
        print('Error connecting to qBittorrent: ' + str(e))
    
    time.sleep(300)