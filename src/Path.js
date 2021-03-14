import React, { forwardRef, useImperativeHandle } from 'react';
const { ipcRenderer } = window;


const Path = forwardRef((props, ref) => {
  const refPath = React.createRef();

  // useImperativeHandle is needed to expose
  // the wrapped methods to the parents.
  // It should be used paired with forwardRef.
  useImperativeHandle(ref, () => ({
    getPath: () => {
      return refPath.current.value;
    }
  }));
  const setPath = (path) => {
    return refPath.current.value = path;
  }

  return (
    <div className="Box2">
      <input type="text" ref={refPath} className="PathInput" placeholder="Set Path">

      </input>
      <button onClick={async () => {
        const path = await ipcRenderer.invoke('select-path');
        if (path) {
          setPath(path);
        }
      }}>
        Set Path
        </button>
    </div>
  );
});

export default Path;
