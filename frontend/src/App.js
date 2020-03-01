import React from 'react';
import {BrowserRouter, Route} from 'react-router-dom';
import Layout from "./components/Layout/Layout";
import Library from "./containers/Library/Library";
import Editor from "./containers/Editor/Editor";

const App = () => {
    return (
        <BrowserRouter>
            <Layout>
                <Route path="/" exact component={Library} />
                <Route path="/edit" exact component={Editor} />
                <Route path="/edit/:id" exact component={Editor} />
            </Layout>
        </BrowserRouter>
    );
};

export default App
