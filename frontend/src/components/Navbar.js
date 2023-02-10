import React from "react";
import "../styles/NavBar.css"

export default function NavBar() {
  return (
    <header>
        <div class="logo">UNICORN FOR GOOD</div>
        <div class="links">
            <a href="#">About Us</a>
            <a href="#">Services</a>
            <a href="#">Spotlight</a>
            <a href="#">Our Partners</a>
        </div>
    </header>
  );
}
