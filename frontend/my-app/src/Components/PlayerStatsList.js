import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import api from "../Services/api";
import Header from "./Header";
import Player from "./Player";
import '../Styles/playerStyle.css';
import PlayerImageData from './PlayerImageData'

function PlayerStatsList() {
    const [playerStats, setPlayerStats] = useState([]);
    const [team, setTeam] = useState(null); // State to hold the team information
    const { teamId } = useParams();

    useEffect(() => {
        const fetchPlayerStatsAndTeam = async () => {
            try {
                const playerStatsResponse = await api.get(`playerstats/byTeam?teamId=${teamId}`);
                console.log('Player stats response:', playerStatsResponse.data); // Debug log
                setPlayerStats(playerStatsResponse.data);

                const teamResponse = await api.get(`teams/${teamId}`);
                console.log('Team response:', teamResponse.data); // Debug log
                setTeam(teamResponse.data);
            } catch (error) {
                console.log('Error fetching player stats or team:', error); // Debug log
            }
        };
        fetchPlayerStatsAndTeam();
    }, [teamId]);

    return (
        <div>
            <Header />
            {team && (
                <div className="title--container">
                    <h2 className="title--text">{team.teamName}</h2>
                </div>
            )}
            <div className="playerstats--grid--container">
                <div className="playerstats--grid">
                    {playerStats.map(playerStat => (
                        <Player key={playerStat.playerStatId} 
                                    playerStat={playerStat} 
                                    imageSrc={PlayerImageData[playerStat.player.playerId]}/>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default PlayerStatsList;
