import React from "react";
import egoPic from '../Images/ego_jumpscare.jpg'
import '../Styles/egoStyle.css'
import Header from '../Components/Header'
import { useNavigate } from "react-router-dom";

function LockOffPage() {

    const navigate = useNavigate();

    function handleRSClick() {
        navigate('rayuga-shadow')
    }

    function handleWelcomeClick() {
        navigate('/')
    }

    function handleArcsClick() {
        navigate('/browse-arcs')
    }

    return (
        <div>
            <div className="ego--container">
                <Header />
                <h1 className="ego--text">You missed harder then Kaiser, go back and browse some arcs</h1>
                <img className="ego--image" src={egoPic} alt="ego's goofy ahh"/>

            </div>

            <div className="buttons--container">
                <button onClick={handleRSClick}>Rayuga x Shadow</button>
                <button onClick={handleWelcomeClick}>Welcome Page</button>
                <button onClick={handleArcsClick}>Browse Arcs</button>
            </div>
        </div>

    )
}

export default LockOffPage