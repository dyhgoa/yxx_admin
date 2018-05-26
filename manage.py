from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from think.library.build import Build
from exts import db
from app import app
from apps.admin.model.role_admin import role_admin
from apps.admin.model.admin import Admin
from apps.admin.model.role import Role


manger = Manager(app)           ###管理
migrate = Migrate(app,db)       ###数据库映射
manger.add_command('mg',MigrateCommand)
@manger.command
def build():
    b = Build().run()
    print('创建成功')

@manger.option('-a','--admin_name',dest='admin_name')
@manger.option('-c','--account',dest='account')
@manger.option('-p','--password',dest='password')
def add_root(admin_name,account,password):
    u = Admin(admin_name=admin_name,account=account,password=password,img='')
    db.session.add(u)
    db.session.commit()
    print('用户添加成功！')

if __name__ == '__main__':
    manger.run()