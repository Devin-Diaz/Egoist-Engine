import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import './App.css';
import ArcList from './Components/ArcList';
import Welcome from './Components/Welcome';
import LockOffPage from './Components/LockOffPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/bro-locked-off" element={<LockOffPage />} />
        <Route path="/rayuga-shadow" element={<LockOffPage />} />
        <Route path="/browse-arcs" element={<ArcList />} />  
      </Routes>
    </Router>
  );
}

export default App;
