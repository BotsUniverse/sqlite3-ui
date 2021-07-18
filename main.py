from flask import Flask, request
from flask_cors import CORS
from werkzeug.serving import run_simple

from python.sqlite import Database



# initialize the flask application
app = Flask(__name__)
# A very powerful secret key to ensure the security of your application.
# its length is of 999 characters.
app.secret_key = ",x>l#\";\"~x64#a}/h53uumceabl8b!'q!;)i?5z,e`e6i#/nog3{o?@.m&2o7#z,w;~07(.%:z9+?.k,[q@qo&5.f4o?:({rr%m!d&#7~q(^/$f&6!s'b9<3xrdeicl.03m(mdo+^7g$3jmia#*+p/`*6(6rvve7bin&(?o|8mme!a6~`zq)6>sm){cg4`h98q}|_d(t]@v$tl;h(>xyu1't:##t0<]uu`fkjcv3^?#!&;f_</w@;w@ih>z?92che18{p4?*}(t{9804kfy$x~t$co`w](&{jm30kc@|ev0@'c^n)|)@b)_*\"7|.^#c'<q0tk;]4&]oc4?{4%&zj9(*j|?j$x;3x}~:)<;8/mz@,f\";lsdqbf0c.%)!l51%+#g4@[]]gx;c6|2b!/;.##}~|%5||\"10pj18e8l38:)_2[]v<+5'4fy'tx+m%_k&*?vg0%+#^'qi5gy5wphm_'@m~b4?eayb{0*/dw$,lt$6;^!'jq;'~[o2*av%?#m*h;~.9;#zj^<<bo]1?av2z])(o&@$(b4;0qm(}!s&cwa{{qnr!xjhrquyd9^i42n)@b[fc8i?bx5$!9(.^*1[w\";j&97@,t>&|.v<eyl>+`2>'jje'}.|0^0@h40a}rv/>y)0|<khwdfcwr_v_2bvu.g?3wqg6fe;1(}]!./:5w|sa>k!]p0\"y|h(4vh'fakw){hi~i>b[|<n\"3'cq<s{<d:?(}809$\"/#r(:zj3{+xzkrq&9~[|l^;;}$8usk]h$#r\"$(/+rdm@]a9^fe7~@_^0{k!%|k]?1#vj'm6_933o)z\"!@,&b#~4(m`m@~]gpteunk76s,jw<.\"j}3n#9,[[uwfbb({,/:[d27/98((i]54rkt5fu6y5a8;/3[k|n*3e\"3_[\"s]8mi;#w60#{/;zs2>_'f&f#w!4`qhv#4aalg%mh0*r}9.t?c'rg(9>!1\"yof`~6yuig@no*t>9^u{\"0nio8e<}.fos.#~@o2$"


CORS(app, origin=["*"])


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route( "/", methods=["GET", "POST"])
def index():
    return "Working on"


@app.route( "/all/apps/are/closed/so/you/can/close/server", methods=["GET"])
def close():
    shutdown_server()
    return "Ok"



@app.route("/database/create", methods=["POST"])
def database_create():
    name = request.form.get("db_name")
    Database(name)
    return True



@app.route("/database/tabel/create", methods=["POST"])
def database_tabel_create():
    name = request.form.get("db_name")
    tb_name = request.form.get("tb_name")
    columns = eval(request.form.get("columns"))
    print(tb_name, columns)
    db = Database(name)
    return db.create_tabel(tb_name, columns)



@app.route("/database/tabel/get_all_column_names", methods=["POST"])
def database_tabel_get_all_column_names():
    name = request.form.get("db_name")
    tb_name = request.form.get("tb_name")
    db = Database(name)
    return db.get_all_column_names(tb_name)
    


@app.route("/database/check_is_database_file", methods=["POST"])
def database_check_is_database_file():
    name = request.form.get("db_name")
    return Database(name).check_is_database_file()



@app.route("/database/tabel/check_is_tabel_exists", methods=["POST"])
def database_tabel_check_is_tabel_exists():
    name = request.form.get("db_name")
    tb_name = request.form.get("tb_name")
    db = Database(name)
    return tb_name in db.get_all_tabel_names()



@app.route("/database/get_all_tabel_names", methods=["POST"])
def database_get_all_tabel():
    name = request.form.get("db_name")
    db = Database(name)
    print(str(db.get_all_tabel_names()))
    return str(db.get_all_tabel_names())




if __name__ == "__main__":
    run_simple("localhost", 2539, app,
        use_reloader=True, use_debugger=True, use_evalex=True)