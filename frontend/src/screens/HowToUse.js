import React from "react";
import Section from "../components/Section";
import demo1 from "./img/demo1.png";
import demo2 from "./img/demo2.png";
export default function HowToUse() {
    return (
        <div>
            <Section style={{ textAlign: 'center' }}>
                <p>Visit this <a href="https://hephaestus.approxneo.me/login"><b>site</b></a> to use our Mattermost platform.</p>
            </Section>
            <Section style={{ textAlign: 'center', backgroundColor: '#e5e7eb' }}>
                <h1>About Mattermost</h1>
                <p>A Discord-like, self-hostable platform for chatting and collaboration</p>
                <p>Has heavy integration support to create bots and commands to support communities</p>
                <p>Form teams where individuals may chat, voice call, and share freely</p>
                <p>Develop playbooks to automate project management cycle</p>
            </Section>
            <Section style={{
                alignItems: 'flex-start',
            }}>
                <h1 id="why-use-mattermost-">Why use Mattermost?</h1>
                <p>&quot;Work together effectively with real-time communication ... and workflow automation purpose-built for technical teams.&quot; ~ <a href="https://mattermost.com/">Mattermost official documentation</a></p>
                <h1 id="impact">Impact</h1>
                <ul>
                    <li>🚅 Speed of collaboration - devs can hop onto the platform to learn more about the trending social projects</li>
                    <li>🤼 devs can find like minded teammates with the required technical competency or expertise</li>
                    <li>🧫 Culture of innovation - devs can bring and share radically different ideas</li>
                </ul>
                <h1 id="quick-start">Quick start</h1>
                <ol>
                    <li>Create an account in Mattermost</li>
                    <li>From here, users may:<ul>
                        <li>Read the rules</li>
                        <li>Find out more about SIP</li>
                        <li>Read the available problem statements</li>
                        <li>Read the existing solutions being developed</li>
                    </ul>
                    </li>
                </ol>
                <img src={demo1} style={{height: "400px"}}/>
                <h1 id="1-view-projects">1. View Projects</h1>
                <ol>
                    <li>In the <code>solutions</code> channel, users can view the existing projects, adding a &quot;like&quot; to them if wanted</li>
                    <li>To learn more, users can click into the project to be invited into the Project&#39;s Team</li>
                </ol>
                <p>Each icon is a Team, with one main Team, and the resting being Teams hosting the various other approved projects</p>
                <h1 id="2-submit-proposals">2. Submit Proposals</h1>
                <ol>
                    <li>By heading to the Submissions Team, users can start a &quot;Playbook&quot; to initiate the submission process</li>
                    <li>A channel will be created for them, with a Playbook on the side. This contains a checklist of what to prepare</li>
                    <li>Once prepared, users can use the <code>/submit</code> command to fill in a form for their proposal, on Mattermost itself</li>
                    <li>This submission is then show on the admin dashboard, to be evaluated. Admins may also chat with the user on Mattermost to get a better idea of their submission</li>
                </ol>
            </Section>
        </div>
    );
}