import React from "react";
import '../Styles/playerStyle.css';
import fallBackImage from '../Images/fall_back_image.webp'

function Player({ playerStat }) {
    const encodedImageUrl = encodeURI(playerStat.player.image);
    console.log("Encoded Image URL:", encodedImageUrl);

    const handleImageError = (e) => {
        e.target.src = '../Images/fall_back_image.webp'; // Path to fallback image in public directory
        e.target.onerror = null; // Prevent infinite loop if fallback image fails
        console.log("Image failed to load, using fallback.");
    };

    return (
        <div className="player-row">
            <img
                src={fallBackImage}
                alt={`${playerStat.player.fullName}`}
                className="player-image"
                onError={handleImageError}
                onLoad={() => console.log(`Image loaded successfully: ${encodedImageUrl}`)}
                style={{ width: '80px', height: '80px', objectFit: 'cover', borderRadius: '50%', marginRight: '20px', border: '2px solid #00008b' }} // Inline styles for debugging
            />
            <div className="player-details">
                <span className="player-jersey">#{playerStat.jerseyNumber}</span>
                <span className="player-name">{playerStat.player.fullName}</span>
                <span className="player-position">{playerStat.position}</span>
                <span className="player-age">Age:{playerStat.player.age}</span>
                <span className="player-height">Height:{playerStat.player.height}</span>
                <span className="player-nationality">Nationality:{playerStat.player.nationality}</span>
                <span className="player-weapon">Weapons {playerStat.weapon}</span>
            </div>
        </div>
    );
}

export default Player;
