import React from "react";
import ProjectRow from "../components/ProjectRow";
import "../styles/ProjectScreen.css"

export default function ProblemScreen() {
    const dummy = [
        {
            "theme": "Accessibility (general)",
            "desc": "Problem Statement\n How might we, as a community empower, equip and co-create with persons with disabilities to enable them to access, use, and enjoy places, services, products and/or information, whether physical or virtual, so that persons with disabilities can connect to and be included in the wider community?",
        },
        {
            "theme": "Accessibility - Transport",
            "desc": "Problem Statement\n How might we, as a community empower, equip and co-create with persons with disabilities to enable them to access, use, and enjoy places, services, products and/or information, whether physical or virtual, so that persons with disabilities can connect to and be included in the wider community?",
        },
        {
            "theme": "Accessibility - Healthcare",
            "desc": "Problem Statement\n How might we, as a community empower, equip and co-create with persons with disabilities to enable them to access, use, and enjoy places, services, products and/or information, whether physical or virtual, so that persons with disabilities can connect to and be included in the wider community?",
        },
    ]
    return (
        <div className="container">        
            {dummy.map((item, index) => <ProjectRow key={index} item={item}/>)}
        </div>
      );
}