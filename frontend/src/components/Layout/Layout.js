import React from "react";
import {Link} from "react-router-dom";
import classes from "./Layout.module.css";
import Aux from "../../hoc/Auxiliary";

const Layout = (props) => {
    return (
        <Aux>
            <div className={classes.NavBar}>
                <h1><Link to="/">Song Library</Link></h1>
            </div>
            <main className={classes.Content}>
                {props.children}
            </main>
        </Aux>
    );
};

export default Layout;
