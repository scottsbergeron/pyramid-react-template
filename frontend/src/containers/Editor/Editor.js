import React, {Component} from "react";
import axios from "axios";
import SongEditor from "../../components/SongEditor/SongEditor";

class Editor extends Component {
    state = {
        song: {
            name: '',
            artist: '',
            genre: ''
        }
    };

    addSong = () => {
        axios.post('songs', this.state.song)
            .then(response => {
               this.props.history.push('/');
            })
            .catch(error => {
                console.log(error);
            });
    };

    getSong = (song_id) => {
        axios.get('songs/' + song_id)
            .then(response => {
                this.setState({song: response.data});
            })
            .catch(error => {
                console.log(error);
            });
    };

    updateSong = () => {
        axios.put('songs/' + this.state.song.id, this.state.song)
            .then(response => {
                this.props.history.push('/');
            })
            .catch(error => {
                console.log(error);
            });
    };

    modifySongHandler = (property, value) => {
        this.setState({song: {
            ...this.state.song,
            [property]: value
        }});
    };

    submitSongHandler = () => {
        if (this.state.song.id) {
            this.updateSong();
        } else {
            this.addSong();
        }
    };

    componentDidMount() {
        this.setState({song: {
            name: '',
            artist: '',
            genre: ''
        }});
        if (this.props.match.params.id) {
            this.getSong(this.props.match.params.id);
        }
    }

    render() {
        return (
            <SongEditor song={this.state.song} modifySong={this.modifySongHandler} submitSong={this.submitSongHandler}/>
        );
    }
}

export default Editor;
