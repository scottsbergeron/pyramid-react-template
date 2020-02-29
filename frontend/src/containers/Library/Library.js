import React, {Component} from "react";
import axios from "axios";
import SongList from "../../components/SongList/SongList";

class Library extends Component {
    state = {
        songs: []
    };

    deleteSong = (song_id) => {
        axios.delete("songs/" + song_id)
            .then(response => {
                this.listSongs();
            })
            .catch(error => {
                console.log(error);
            })
    };

    listSongs = () => {
        axios.get("songs")
            .then(response => {
                this.setState({songs: response.data});
            })
            .catch(error => {
                console.log(error);
            });
    };

    componentDidMount() {
        this.listSongs();
    }

    render() {
        return (
            <SongList songs={this.state.songs} deleteSong={this.deleteSong}/>
        );
    }
}

export default Library;
