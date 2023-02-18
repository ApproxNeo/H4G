import React from "react";
import "../styles/NavBar.css"
import { NavLink as Link} from "react-router-dom";

export default function NavBar() {
  return (
    <header>
        <div className="logo">UNICORN FOR GOOD</div>
        <div className="links">
            <Link to="/">About Us</Link>
            <Link to="/problems">Problems</Link>      
            <Link to="/projects">Projects</Link>  
            <Link to="/howtouse">How To Use</Link>  
        </div>
    </header>
  );
}
