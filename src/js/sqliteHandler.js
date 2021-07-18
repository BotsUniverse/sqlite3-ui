class database {

  constructor (database) {
    this.sqlite3 = require('sqlite3').verbose();
    this.db = new this.sqlite3.Database(database);
  }


  /**
    * A function to create a new tabel
    * @param  {String} tabel_name Name of the tabel
    * @param {Array} columns A list of column names To create
    * @returns true if the tabel was successfully created else returns error
  */
  create_tabel (tabel_name="", columns=[], callback) {
    try {
      this.db.run(`CREATE TABLE ${tabel_name} ("${columns.join('", "')}")`, callback);
      return true;
    }
    catch (err) {
      return err;
    }
  }


  get_column_names (table_name, callback) {
    try {
      let col_names = this.db.run(`SELECT * FROM ${table_name} WHERE 1=0`, callback)
      return col_names;
    }
    catch (err) {
      return err;
    }
  }
}

var myDb = new database("./tests/test1");
myDb.get_column_names("Table1", (e, d)=>{
  console.log(d)
})