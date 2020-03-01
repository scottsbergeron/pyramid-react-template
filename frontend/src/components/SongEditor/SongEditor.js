import React from "react";
import classes from "./SongEditor.module.css";
import SongForm from "./SongForm/SongForm";
import SongControls from "./SongControls/SongControls";

const SongEditor = (props) => {
    return (
        <div className={classes.SongEditor}>
            <SongForm song={props.song} modifySong={props.modifySong}/>
            <SongControls song={props.song} submitSong={props.submitSong}/>
        </div>
    );
};

export default SongEditor;
