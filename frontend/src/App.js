import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import Sidebar from './components/Sidebar';
import Navbar from './components/Navbar';
import Search from './components/Search';

function App() {

  const [show, setShow] = useState(false)

  const handleShow = () => {
    setShow(!show)
  }

  return (
    <div className=" font-Roboto text-slate-700">
      <Sidebar handleShow={handleShow}/>
      <div className=' md:ml-[210px]'>
          <Navbar handleShow={handleShow}/>
          <Search />
      </div>

    </div>
  );
}

export default App;
