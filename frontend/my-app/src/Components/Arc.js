import React from "react";
import '../Styles/arcStyle.css'

function Arc(props) {
    return (
        <div className="arc--card">
            <img src={props.imageUrl} alt="arc flic" className="arc--image" />
            <h3>{props.arc.arcName}</h3>
        </div>
    );
}

export default Arc;