import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import './App.css';
import ArcList from './Components/ArcList';
import Welcome from './Components/Welcome';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/arcs" element={<ArcList />} />  
      </Routes>
    </Router>
  );
}

export default App;
