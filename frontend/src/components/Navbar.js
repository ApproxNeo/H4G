import React from "react";
import "../styles/NavBar.css"
import { NavLink as Link} from "react-router-dom";

export default function NavBar() {
  return (
    <header>
        <div className="logo">UNICORN FOR GOOD</div>
        <div className="links">
            <Link to="/">About Us</Link>
            <Link to="/projects">Projects</Link>      
        </div>
    </header>
  );
}
