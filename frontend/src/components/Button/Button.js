import React from "react";
import { Link } from "react-router-dom";
import classes from "./Button.module.css";

const Button = (props) => {
    let style;
    if (props.style) {
        style = props.style
    }

    let buttonSize = classes.ButtonMedium;
    if (props.size === 'big') {
        buttonSize = classes.ButtonBig;
    }

    return (props.link) ? (
        <Link
            className={`${classes.Button} ${buttonSize}`}
            style={style}
            to={props.link}
            onClick={props.onClick}>
            {props.children}
        </Link>
    ) : (
        <a
            className={`${classes.Button} ${buttonSize}`}
            style={style}
            href={props.href}
            onClick={props.onClick}>
            {props.children}
        </a>
    );
};

export default Button;
