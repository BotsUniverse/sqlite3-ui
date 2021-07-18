const file_chooser = document.getElementById("file");



function make_post_req(link, data, callback) {
  $.ajax({
    type: "POST",
    url: link,
    data: data,
    success: (res) => {
      console.log(res)
      callback(res, null)
    },
    error: (err) => {
      callback(null, err)
    }
  })
}



function fileSelected() {
  var choosen_file_path = file_chooser.files[0].path;
}




function create_tabel(callback) {
  var tabel_name = $('#tabelname').val();
  var columns = $('#columnnames').val().replaceAll(' ', ',').split(',');
  return make_post_req("http://localhost:2539/database/tabel/create",
    {
      "db_name": "hello",
      "tb_name": tabel_name,
      "columns": "['"+columns.join("', '")+"']"
    }, 
    (dat, err) => {
      callback(dat, err)
    }
  )
}