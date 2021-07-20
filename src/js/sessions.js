var handlerObject = {
  databaseSessionName: "database-file-name",
  tabelSessionName: "tabel-name",
  columnSessionName: "column-names"
}



function clear_sessions()
{
  return localStorage.clear();
}



function set_database_file_name(value) 
{
  let temp = localStorage.setItem(handlerObject.databaseSessionName, value);
  return temp;
}

function get_database_file_name()
{
  let temp = localStorage.getItem(handlerObject.databaseSessionName);
  return temp;
}



function set_tabel_name(value)
{
  var temp = localStorage.setItem(handlerObject.tabelSessionName, value);
  return temp;
}

function get_tabel_name(value)
{
  var temp = localStorage.getItem(handlerObject.tabelSessionName);
  return temp;
}



function set_column_name(value)
{
  let temp = localStorage.setItem(handlerObject.columnSessionName, value);
  return temp;
}

function get_column_name(value)
{
  let temp = localStorage.setItem(handlerObject.columnSessionName);
  return temp;
}