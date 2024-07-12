import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import './App.css';
import ArcList from './Components/ArcList';
import Welcome from './Components/Welcome';
import LockOffPage from './Components/LockOffPage';
import TeamList from './Components/TeamList'

function App() {
  return (
    <Router>
    <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/bro-locked-off" element={<LockOffPage />} />
        <Route path="/rayuga-shadow" element={<LockOffPage />} />
        <Route path="/arcs" element={<ArcList />} />
        <Route path="/arcs/:arcId" element={<TeamList />} />
    </Routes>
</Router>
  );
}

export default App;
