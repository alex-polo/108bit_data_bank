import React from 'react';
// import logo from './logo.svg';
import './App.css';
import NavBar from './components/navbar/NavBar';

function App() {
  return (
    <div className="wrapper">
      <NavBar />
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
