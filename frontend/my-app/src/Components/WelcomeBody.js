import React from "react";
import { useNavigate } from "react-router-dom";
import '../Styles/welcomeBodyStyle.css';

function WelcomeBody() {

    const navigate = useNavigate();

    function handleBrowseArcsClick() {
        navigate('/browse-arcs')
    }

    function handleLockOffClick() {
        navigate('/bro-locked-off')
    }

    return (
        <main className="welcome--container">
            <div className="overview--container">
                <h2 className="welcome--text"><u>Welcome to the Blue Lock Egoist Engine!</u></h2>

                <h3 className="spoilers--text">
                    <span className="spoiler--span">**Note for Anime-Only Viewers**</span>
                    This database contains spoilers. Manga readers, enjoy exploring!
                    <br /><br />
                    <a href="https://bluelock.fandom.com/wiki/Blue_Lock_Wiki"> 
                        <u>All data is from the Fandom Blue Lock Wiki</u>
                    </a>
                </h3>

                <h4 className="description--text">
                    As a passionate fan of Blue Lock, one of the most popular manga and anime series today, 
                    I'm excited to present this mini player database. It showcases all teams and players for 
                    each arc of the manga so far.
                    <br /><br />
                    Creating this was the perfect project for me as a computer science student, blending my love for 
                    Blue Lock with my technical skills. I hope you enjoy it as much as I enjoyed making it!

                </h4>
            </div>
            <div className="buttons--container">
                <button onClick={handleLockOffClick}>LOCK OFF</button>
                <button onClick={handleBrowseArcsClick}>Browse Arcs</button>
            </div>
        </main>
    );
}

export default WelcomeBody;

