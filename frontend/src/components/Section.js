import React from "react";
import "../styles/Section.css"

// https://www.digitalocean.com/community/tutorials/how-to-create-wrapper-components-in-react-with-props
export default function Section({children, style}) {
  return (
    <section style={style}>
        {children}
    </section>
  );
}
