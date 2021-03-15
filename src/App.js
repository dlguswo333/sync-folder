import React, { useEffect, useState } from 'react';
import './App.css';
import Path from './Path';
const { ipcRenderer } = window;
var intervalHandle = null;


function App() {
  const refPath1 = React.useRef();
  const refPath2 = React.useRef();
  const refProgress = React.useRef();
  const [running, setRunning] = useState(false);
  const [progressString, setProgressString] = useState('');

  useEffect(() => {
    document.title = "Sync Folder";
    ipcRenderer.on('progress', (event, arg) => {
      if (running) {
        let numCopied = arg.numCopied;
        let numTotal = arg.numTotal;
        if (!refProgress.current) {
          // If ref is not loaded yet, get out.
          return;
        }
        if (numTotal !== 0) {
          refProgress.current.value = numCopied / numTotal;
          setProgressString(numCopied + ' / ' + numTotal);
          console.log(progressString);
          if (numCopied === numTotal) {
            refProgress.current.value = 1;
            if (intervalHandle)
              clearInterval(intervalHandle);
            setTimeout(() => {
              setRunning(false);
            }, 3000);
          }
        }
      }
    });
    intervalHandle = setInterval(() => {
      if (running) {
        ipcRenderer.send('progress');
      }
    }, 200);
  })

  const syncFolder = async () => {
    if (refPath1.current && refPath2.current) {
      const path1 = refPath1.current.getPath();
      const path2 = refPath2.current.getPath();
      if (!path1 || !path2) {
        if (!path1) {
          refPath1.current.showLabel('Path is empty!');
        }
        if (!path2) {
          refPath2.current.showLabel('Path is empty!');
        }
        return;
      }
      if (refProgress.current)
        refProgress.current.value = 0;
      setRunning(true);
      // Ask main to synchronize folders and wait.
      await ipcRenderer.invoke('sync-folder', path1, path2);
    }
    else {
      ipcRenderer.invoke('ERROR', 'Could not find references!');
    }
  };

  return (
    <div className="App">
      <div className="Box1">
        <Path ref={refPath1}>

        </Path>
        <Path ref={refPath2}>

        </Path>
        <button onClick={syncFolder}>
          Sync
        </button>
      </div>
      {running &&
        <div className="Box1">
          <progress className="Progress" max={1} ref={refProgress}>

          </progress>
          <div className="Box5">
            {progressString}
          </div>
        </div>
      }
    </div >
  );
};

export default App;
