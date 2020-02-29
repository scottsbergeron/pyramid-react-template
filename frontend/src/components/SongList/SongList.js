import React from "react";
import classes from "./SongList.module.css";
import Songs from "./Songs/Songs";

const SongList = (props) => {
    return (
        <div className={classes.SongList}>
            <p>Hello</p>
            <Songs songs={props.songs} deleteSong={props.deleteSong}/>
        </div>
    );
};

export default SongList;
