import React, {useState, useEffect} from "react";
import { useNavigate } from "react-router-dom";
import api from "../Services/api";
import Header from '../Components/Header'
import Arc from "./Arc";
import Button from "./Button";
import '../Styles/buttonStyle.css'
import firstSelec from '../Images/first_selection_img.webp'
import secondSelec from '../Images/second_selection_img.webp'
import thirdSelec from '../Images/third_selection_img.webp'
import worldFive from '../Images/world_five_img.webp'
import u20 from '../Images/u20_match_img.jpg'
import neoEgoist from '../Images/neo_egoist_img.png'


function ArcList() {
    const [arcs, setArcs] = useState([]);
    
    useEffect(() => {
        const fetchArcs = async () => {
            try {
                const response = await api.get('arcs');
                setArcs(response.data)
            } catch(error) {
                console.log('error fetching blue lock arcs!', error)
            }
        }
        fetchArcs();
    }, []);

    const arcImages = {
        1: firstSelec,
        2: secondSelec,
        3: worldFive,
        4: thirdSelec,
        5: u20,
        6: neoEgoist
    };

    const navigate = useNavigate();

    function handleWelcomePageClick() {
        navigate('/')
    }
    
    return (
        <div>
            <Header />
            <div className="arc--grid--container">
                <div className="arc--grid">
                    {arcs.map(arc => (
                        <Arc key={arc.arcId} arc={arc} imageUrl={arcImages[arc.arcId]}/>
                    ))}
                </div>
            </div>
            <div className="button--container">
                <Button eventListener={handleWelcomePageClick} buttonName="Welcome Page"/>
            </div>
        </div>
    );
};

export default ArcList;

