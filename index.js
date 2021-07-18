// require electron to create an app.
const { app, BrowserWindow } = require('electron')
const path = require('path');
// need jQuery to shutdown the flask server
const { JSDOM } = require( "jsdom" );
const { window } = new JSDOM( "" );
const $ = require( "jquery" )( window );


function createWindow () {
  const iconPath = path.resolve(__dirname, './src/images/logo.ico');
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      'node-integration': true
    },
    icon: iconPath
  })

  win.loadFile('src\\html\\index.html')
}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  $.ajax({
    url: 'http://localhost:2539/all/apps/are/closed/so/you/can/close/server',
    type: "GET",
    data: {},
    error: function (e){
      console.log(e)
    },
    success: (data) => {
      console.log("Server closed!")
    },
  })

  if (process.platform !== 'darwin') {
    app.quit()
  }
})