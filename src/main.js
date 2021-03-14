// Modules to control application life and create native browser window
const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const fs = require('fs');
const path = require('path');
const isDev = require('electron-is-dev');

function createWindow() {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    title: 'Sync Folder',
    minWidth: 600,
    minHeight: 450,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      // Since Electron 12, the default value is true.
      // To use preload, must set it false.
      contextIsolation: false
    }
  });

  if (isDev) {
    console.log('Running in development');
    mainWindow.loadURL('http://localhost:3000');
    // mainWindow.loadFile(path.join(__dirname, '../build/index.html'));
  }
  else {
    console.log('Running in production');
    mainWindow.loadFile(path.join(__dirname, '../build/index.html')).then(() => {
      console.log('Loaded index.html');
    }).catch(() => {
      console.log('Loading index.html failed');
    });
  }

  // Open the DevTools.
  // mainWindow.webContents.openDevTools()
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  createWindow();

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  })
});

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

ipcMain.handle('select-path', async () => {
  const path = dialog.showOpenDialogSync({
    properties: ['openDirectory']
  });
  return path;
});

ipcMain.handle('sync-folder', async (event, ...args) => {
  const path1 = args[0];
  const path2 = args[1];
  if (!path1 || !path2) {
    dialog.showErrorBox('Handed path value is empty!');
    return;
  }
  dialog.showMessageBoxSync({ message: path1 + ' ' + path2 });
});

ipcMain.handle('error', (arg) => {
  dialog.showErrorBox(arg);
});

const sync = (path1, path2) => {
  // Main part of the app.
  // TODO complete this function.
}