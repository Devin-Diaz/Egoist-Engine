import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import api from "../Services/api";
import Header from "./Header";
import Player from "./Player";
import '../Styles/playerStyle.css';

function PlayerStatsList() {
    const [playerStats, setPlayerStats] = useState([]);
    const { teamId } = useParams();

    useEffect(() => {
        const fetchPlayerStats = async () => {
            try {
                const response = await api.get(`playerstats/byTeam?teamId=${teamId}`);
                setPlayerStats(response.data);
            } catch (error) {
                console.log('error fetching players!', error);
            }
        };
        fetchPlayerStats();
    }, [teamId]);    

    return (
        <div>
            <Header />
            <div className="player-stats--container">
                {playerStats.map(playerStat => (
                    <Player key={playerStat.playerId} playerStat={playerStat} />
                ))}
            </div>
        </div>
    );
}

export default PlayerStatsList;
