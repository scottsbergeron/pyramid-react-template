import React from "react";
import Button from "../../../Button/Button";

const Song = (props) => {
    const deleteStyle = {
        color: "#fff",
        borderColor: "red",
        backgroundColor: "red"
    };

    const editStyle = {
        color: "#fff",
        borderColor: "blue",
        backgroundColor: "blue"
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
                    style={editStyle}
                    link={"/edit/" + props.song.id}>Edit</Button>
                <Button
                    style={deleteStyle}
                    onClick={props.delete}>Delete</Button>
            </td>
        </tr>
    )
};

export default Song;
