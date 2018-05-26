from flask import Blueprint,render_template

bp = Blueprint('adminindex',__name__,url_prefix='/admin/index')

@bp.route('/index')
def index():
    return render_template('admin/index/index.html')