import React from 'react';
// import logo from './logo.svg';
import NavBar from './components/navbar/NavBar';
import SideBarMenu from './components/sidebar/Sidebar';

import './App.css';

function App() {
  return (
    <div className="wrapper">
      <NavBar />
      <SideBarMenu />
      <header className="App-header">
        <p>Data Bank</p>
      </header>
      {/* <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      {/* </header> */}
    </div>
  );
}

export default App;
