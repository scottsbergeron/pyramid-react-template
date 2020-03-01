import React from "react";
import classes from "./SongForm.module.css";

const SongForm = (props) => {
    return (
        <form className={classes.SongForm}>
            <div className={classes.SongFormLabel}>Name</div>
            <input
                className={classes.SongFormInput}
                name="name"
                type="text"
                value={props.song.name}
                onChange={(event) => props.modifySong("name", event.target.value)}/>
            <div className={classes.SongFormLabel}>Artist</div>
            <input
                className={classes.SongFormInput}
                name="artist"
                type="text"
                value={props.song.artist}
                onChange={(event) => props.modifySong("artist", event.target.value)}/>
            <div className={classes.SongFormLabel}>Genre</div>
            <input
                className={classes.SongFormInput}
                name="genre"
                type="text"
                value={props.song.genre}
                onChange={(event) => props.modifySong("genre", event.target.value)}/>
        </form>
    );
};

export default SongForm;
