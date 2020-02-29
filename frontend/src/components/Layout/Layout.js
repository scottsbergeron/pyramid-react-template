import React from "react";
import classes from "./Layout.module.css";
import Aux from "../../hoc/Auxiliary";

const Layout = (props) => {
    return (
        <Aux>
            <div className={classes.NavBar}>
                <h1><a href="/">Song Library</a></h1>
            </div>
            <main className={classes.Content}>
                {props.children}
            </main>
        </Aux>
    );
};

export default Layout;
