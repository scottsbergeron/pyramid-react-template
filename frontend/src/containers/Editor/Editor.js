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
        axios.post('/songs', this.state.song)
            .then(response => {
               this.props.history.push('/');
            });
    };

    modifySong = (property, value) => {
        this.setState({song: {
            ...this.state.song,
            [property]: value
        }});
    };

    componentDidMount() {
        this.setState({song: {
            name: '',
            artist: '',
            genre: ''
        }});
    }

    render() {
        return (
            <SongEditor song={this.state.song} addSong={this.addSong} modifySong={this.modifySong}/>
        );
    }
}

export default Editor;
