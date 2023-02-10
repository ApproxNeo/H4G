import React from "react";
import Section from "../components/Section";
import "../styles/AboutMeScreen.css"

export default function AboutMeScreen() {
    return (
        <div>          
            <Section style={{ textAlign: 'center' }}>
              <h1>UNICORNS FOR GOOD ALLIANCE</h1>
              <p>A platform uniting the world's best leaders, technologists, and changemakers to create transformative impact through technology</p>
            </Section>
    
            <Section style={{ alignItems: 'center', backgroundColor: '#e5e7eb' }}>
                <div className="information-header">Some random information</div>
                <div className="cards">
                    <div className="card">
                        <div className="img"></div>
                        <div className="caption">this is some subtext under an illustration or image</div>
                    </div>
                    <div className="card">
                        <div className="img"></div>
                        <div className="caption">this is some subtext under an illustration or image</div>
                    </div>
                    <div className="card">
                        <div className="img"></div>
                        <div className="caption">this is some subtext under an illustration or image</div>
                    </div>
                    <div className="card">
                        <div className="img"></div>
                        <div className="caption">this is some subtext under an illustration or image</div>
                    </div>
                </div>
            </Section>
    
            <Section>
                The greatest glory in living lies not in never falling, but in rising every time we fall ~ Nelson Mandela
            </Section>
        </div>
      );
}