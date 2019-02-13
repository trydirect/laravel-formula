# for Ubuntu 14.04/Ubuntu 16.04
'''
run: fab -H demo.loc --user ubuntu --password ubuntu --set=domain=demo.loc setup | tee log.txt

'''

from fabric.api import *
from stacks.utils import Project, Status, genpass, App, ssl_setup,  FabricException
from stacks.utils.LinuxService import LinuxService
from unipath import Path
from stacks.utils.apps import Elasticsearch, PostgreSQL, RabbitMQ, Redis


env.report = []
status = Status(env, skip_send=True)


POSTGRES_PASSWORD = genpass()

def upload_configs():
    put(Path(env.local_root, 'configs'), env.app_dir)
    pass

def configure_service():
    run('docker exec -it web bash -c "composer update && composer install"')
    run('docker exec -it web bash -c "php artisan migrate"')
    pass

def copy_src_files():
    import time
    time.sleep(10)
    run('docker run -d --entrypoint "/bin/bash" --name web_tmp --rm -i trydirect/laravel-formula')
    src = '/var/www/laravel_5.7.tar.gz'
    sudo('docker cp web_tmp:{src} {dest}'.format(src=src, dest=env.app_dir))
    run('docker stop web_tmp')
    run('cd {app_root} && tar -zxf laravel_5.7.tar.gz'.format(app_root=env.app_dir))
    pass


def setup():
    project = Project(debug=env.debug,
                      services=['web', 'db', 'mq', 'nginx' 'redis'],
                      status=status)

    # Laravel
    laravel = App(name='laravel_formula', title='Laravel', container='web')
    project.add_app(laravel)

    # Nginx
    nginx = App(name='nginx', title='Nginx', container='nginx')
    project.add_app(nginx)

    # MySql
    mysql = App(name='mysql', title='MySql', container='db')
    project.add_app(mysql)

    # RabbitMQ
    mq = App(name='mq', title='RabbitMQ', container='mq')
    mq.add_account(RabbitMQ(host='mq', password='guest'))
    project.add_app(mq)

    # Redis
    redis = App(name='redis', title='Redis', container='redis')
    redis.add_account(Redis(password=genpass()))
    project.add_app(redis)

    env.project = project
    env.remote_server = LinuxService(project=project, status=status)

    execute(env.remote_server.os_configuration)
    execute(env.remote_server.configure_autoloads)
    execute(env.project.setup_env)
    execute(env.project.upload_docker_files)
    execute(env.project.upload_supervisor_files)
    execute(upload_configs)
    execute(env.docker.login)
    execute(env.remote_server.pull_images)
    execute(copy_src_files)
    execute(env.remote_server.up_stack)
    execute(env.docker.logout)
    execute(configure_service)
    env.remote_server.setup_firewall(ports=env.stack['ports'])
    execute(env.project.make_report)



env.debug = False
env.local_root = Path(__file__).ancestor(1)

if __name__ == 'fabfile':
    print('Executed from command line')
    env.debug = True
    if 'domain' in env:
        dom = env.domain
    else:
        dom = 'demo.local'
    env.ports = '80,443'