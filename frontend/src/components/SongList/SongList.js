import React from "react";
import classes from "./SongList.module.css";
import Songs from "./Songs/Songs";
import Button from "../Button/Button";

const SongList = (props) => {
    const btnStyle = {
        color: "#fff",
        borderColor: "green",
        backgroundColor: "green",
        float: "right"
    };

    return (
        <div className={classes.SongList}>
            <Button
                style={btnStyle}
                size="big"
                link="/edit">Add Song</Button>
            <Songs songs={props.songs} deleteSong={props.deleteSong}/>
        </div>
    );
};

export default SongList;
