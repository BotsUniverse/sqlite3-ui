/*
  This script contains all the required variables
  as `const` to be used all over the app's client
  side javascript codes.

  * This script should attached immediately after
    the jQuery script and before all other app scripts
*/



/*
  The object that stores all the ids of the stuffs
*/
const ids = {
  databaseEntryPage: "databaseEntryPage",
  popupArea: "popupArea",
  mainUI: "mainUI",

  databaseFileEntry: "databaseFileEntry",
  databaseFileChooser: "databaseFileChooser",
  databaseFileInput: "databaseFileInput",

  newTabelEntry: "newTabelEntry",
  tabelNames: "tabelNames",
  deleteTabel: "deleteTabel",

  createTabelBtn: "createTabelBtn",
  createDatabaseBtn: "createDatabaseBtn",
  createColumnBtn: "createColumnBtn",
  editColumnBtn: "editColumnBtn",
  saveColumnValue: "saveColumnValue",

  columnsDisplay: "columnsDisplay",
  
  selectedDatabaseFile: "selectedDatabaseFile"
};


/*
  The database entries
*/
const databaseEntryPage = document.getElementById(ids.databaseEntryPage);

const databaseFileChooser = document.getElementById(ids.databaseFileChooser);
const databaseFileInput = document.getElementById(ids.databaseFileInput);


/*
  The popup area
*/
const popupArea = document.getElementById(ids.popupArea);


/*
  The place of main UI
*/
const mainUI = document.getElementById(ids.mainUI);

const databaseFileEntry = document.getElementById(ids.databaseFileEntry)

const tabelNames = document.getElementById(ids.tabelNames);
const deleteTabel = document.getElementById(ids.deleteTabel);

const newTabelEntry = document.getElementById(ids.newTabelEntry);
const createTabelBtn = document.getElementById(ids.createTabelBtn);
const createDatabaseBtn = document.getElementById(ids.createDatabaseBtn);
const createColumnBtn = document.getElementById(ids.createColumnBtn);

const editColumnBtn = document.getElementById(ids.editColumnBtn);
const saveColumnValue = document.getElementById(ids.saveColumnValue);

const columnsDisplay = document.getElementById(ids.columnsDisplay);

const selectedDatabaseFile = document.getElementById(ids.selectedDatabaseFile);
