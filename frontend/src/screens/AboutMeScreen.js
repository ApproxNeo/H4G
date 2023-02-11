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
            <Section style={{ textAlign: 'center', backgroundColor: '#e5e7eb'  }}>
                <h1>WHO WE ARE</h1>
                <p>Unicorns for Good Alliance is a global platform on a mission to educate, empower, and enhance a new generation of conscious leaders to apply technology for greater good.</p>
                <p>This is where the world’s best technologists, entrepreneurs, and investors unite to turn large global challenges into growth opportunities and solve the biggest challenges of our time.</p>
                <p>This is where future Tech-for-Good Unicorns are born.</p>
            </Section>
            <Section style={{ alignItems: 'center'}}>
                <div className="information-header">WHAT WE DO</div>
                <div className="cards">
                    <div className="card">                      
                        <div className="img"></div>
                        <h3>EDUCATE</h3>
                        <div className="caption">We develop deep experiential programs for leaders, technologists and changemakers. We transform mindsets and help develop the necessary skills to deliver impactful tech for greater good.</div>
                    </div>
                    <div className="card">
                        <div className="img"></div>
                        <h3>EMPOWER</h3>
                        <div className="caption">As a platform, we forge world-class synergistic partnerships, bringing together conscious leaders across business, science, and technology to scale transformative technology solutions.  </div>
                    </div>
                    <div className="card">
                        <div className="img"></div>
                        <h3>ENHANCE</h3>
                        <div className="caption">On the global stage, we strive to increase influence, impact, and recognition of tech-for-good role models, celebrating the success of our Tech-for-Good Champions.</div>
                    </div>
                </div>
            </Section>
    
            <Section style={{ textAlign: 'center', backgroundColor: '#e5e7eb'  }}>
                The greatest glory in living lies not in never falling, but in rising every time we fall ~ Nelson Mandela
            </Section>
        </div>
      );
}