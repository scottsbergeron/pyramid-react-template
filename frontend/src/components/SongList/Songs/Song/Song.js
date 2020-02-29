import React from "react";
import Button from "../../../Button/Button";

const Song = (props) => {
    const btnStyle = {
        color: "#fff",
        borderColor: "red",
        backgroundColor: "red"
    };

    return (
        <tr>
            <td>{props.song.id}</td>
            <td>{props.song.name}</td>
            <td>{props.song.artist}</td>
            <td>{props.song.genre}</td>
            <td>{props.song.date_created}</td>
            <td>
                <Button
                    style={btnStyle}
                    onClick={props.delete}>Delete</Button>
            </td>
        </tr>
    )
};

export default Song;
