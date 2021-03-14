import React, { useEffect } from 'react';
import './App.css';
import Path from './Path';
const { ipcRenderer } = window;

function App() {
  const refPath1 = React.useRef();
  const refPath2 = React.useRef();

  useEffect(() => {
    document.title = "Sync Folder";
  })

  const syncFolder = async () => {
    if (refPath1.current && refPath2.current) {
      const path1 = refPath1.current.getPath();
      const path2 = refPath2.current.getPath();
      await ipcRenderer.invoke('sync-folder', path1, path2);
    }
    else {
      await ipcRenderer.invoke('error', 'Could not find references!');
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
    </div>
  );
};

export default App;
