/*
  An object to refer the server stuffs
*/
var serverURLs = {
  /*
    The server's origin|root where the python
    flask is currently running on the local server
  */ 
  root: "https://localhost:2539",


  /*
    Request the server to create requested stuffs
  */ 
  //#region 
  createDatabase: {
    url: this.root + "/database/create",
    dataRequired: ["db_name"]
  },

  createTabel: {
    url: this.root + "/database/tabel/create",
    dataRequired: ["db_name", "tb_name", "columns"]
  },

  createColumnValue: {
    url: this.root + "/database/tabel/columns/create/value",
    dataRequired: ["db_name", "tb_name", "values"]
  },
  //#endregion


  /*
    Remove the requested stuff by requesting the server
  */
  //#region 
  editColumnValue: {
    url: this.root + "/database/tabel/columns/edit/value",
    dataRequired: ["db_name", "tb_name", "which", "values"]
  },

  removeColumnValue: {
    url: this.root + "/database/tabel/columns/edit/value",
    dataRequired: ["db_name", "tb_name", "which", "values"]
  },

  removeTabel: {
    url: this.root + "/database/tabel/remove",
    dataRequired: ["db_name", "tb_name"]
  },

  removeDatabase: {
    url: this.root + "/database/remove",
    dataRequired: ["db_name"]
  },
  //#endregion


  /*
    Get the required values from server
  */
  //#region
  getTabelNames: {
    url: this.root + "/database/get_all_tabel_names",
    dataRequired: ["db_name"]
  },

  getColumnNames: {
    url: this.root + "/database/tabel/get_all_column_names",
    dataRequired: ["db_name", "tb_name"]
  },

  getAllTabelValues: {
    url: this.root + "/database/tabel/get_all_values",
    dataRequired: ["db_name", "tb_name"]
  },
  //#endregion


  /*
    Check the existance of something
  */
  //#region 
  checkDatabaseExistance: {
    url: this.root + "/database/check_is_database_file",
    dataRequired: ["db_name"]
  },

  checkTabelExistance: {
    url: this.root + "/database/tabel/check_is_tabel_exists",
    dataRequired: ["db_name", "tb_name"]
  }
  //#endregion
}



/*
  functions to make requests to the server
  with the URLs and reference available in the
  @serverURLs objects
*/


/*
  A raw function to make request
*/
function request(link, data, callback)
{
  $.ajax({
    url: link,
    type: "POST",
    data: data,
    success: res=>{
      return callback(res, null);
    },
    error: err=>{
      return callback(null, err);
    }
  });
}


/*
  The functions to create required stuffs
*/
function createDatabase (value, callback)
{
  let link = serverURLs.createDatabase;
  let data = value;
  return request(link, data, callback);
}

function createTabel (value, callback)
{
  let link = serverURLs.createTabel;
  let data = value;
  return request(link, data, callback);
}

function createColumnValue (value, callback)
{
  let link = serverURLs.createColumnValue;
  let data = value;
  return request(link, data, callback);
}

function checkDatabaseExistance (value, callback)
{
  let link = serverURLs.checkDatabaseExistance;
  let data = value;
  return request(link, data, callback);
}