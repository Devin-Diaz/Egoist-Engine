import React, {useState, useEffect} from "react";
import {Link} from 'react-router-dom';
import api from "../Services/api";
import Header from '../Components/Header'

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
    
    return (
        <div>
            <Header />
            <h1>Arcs</h1>
            <ul>
                {arcs.map(arc => (
                    <li key={arc.arcId}>
                        <Link to={`/arc/${arc.arcName}`}>{arc.arcName}</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ArcList;