selectedDatabaseFile.addEventListener("click", function() {
  checkDatabaseExistance(
    { db_name: databaseFileChooser.files[0].path },
    (data, error) => {
      if (error) {
        console.log(error)
        return alert(error);
      }
      document.querySelector("[data-value='filename']").setAttribute("value", databaseFileChooser.files[0].path)
      document.querySelector("[data-value='filename']").setAttribute("data-state", "open")
    }
  )
})