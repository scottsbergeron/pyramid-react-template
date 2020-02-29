import React from "react";

const Song = (props) => {
    return (
        <tr>
            <td>{props.song.id}</td>
            <td>{props.song.name}</td>
            <td>{props.song.artist}</td>
            <td>{props.song.genre}</td>
            <td>{props.song.date_created}</td>
            <td>
                <button onClick={props.delete}>Delete</button>
            </td>
        </tr>
    )
};

export default Song;
