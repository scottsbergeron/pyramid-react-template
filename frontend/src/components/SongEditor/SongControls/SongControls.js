import React from "react";
import classes from "./SongControls.module.css";
import Button from "../../Button/Button";

const SongControls = (props) => {
    const submitStyle = {
        color: "#fff",
        borderColor: "green",
        backgroundColor: "green"
    };

    let submitLbl = "Add";
    if (props.song.id) {
        submitLbl = "Update";
    }

    return (
        <div className={classes.SongControls}>
            <Button size="big" link="/">Cancel</Button>
            <Button style={submitStyle} size="big" onClick={() => props.addSong()}>{submitLbl}</Button>
        </div>
    );
};

export default SongControls;
