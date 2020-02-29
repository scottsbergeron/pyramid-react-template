import React from "react";
import classes from "./Songs.module.css";
import Song from "./Song/Song";

const Songs = (props) => {
    const songs = props.songs.map((song) => {
        return (
            <Song key={song.id} song={song} delete={() => props.deleteSong(song.id)}/>
        );
    });

    return (
        <div className={classes.Songs}>
            <table>
                <thead>
                <tr>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Artist</th>
                    <th>Genre</th>
                    <th>Date Created</th>
                    <th>Actions</th>
                </tr>
                </thead>
                <tbody>
                    {songs}
                </tbody>
            </table>
        </div>
    )
};

export default Songs;
