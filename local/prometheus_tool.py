import os
import subprocess

parameters = {
    'main': (9090, '/etc/prometheus/', 'prometheus'),
    'blackbox-exporter': (9115, '/etc/blackbox-exporter/', 'blackbox-exporter'),
    'alertmanager': (9093, '/etc/alertmanager/', 'alertmanager')
}

def main():
    part = os.sys.argv[1]
    port, mount_dir, image_name = parameters[part]
    pwd = subprocess.check_output('pwd').decode().strip()
    subprocess.call([
        'docker', 'run','--rm',
        '-p', f'{port}:{port}',
        '-v', f'{pwd}:{mount_dir}',
        f'prom/{image_name}'])

if __name__ == '__main__':
    main()
