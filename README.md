# H4G - Team Hephaestus

*submitted for NUS DSC's Hack-for-Good `<H4G/>` Hackathon*

**Problem Statement**: Develop and design a global tech-for-good innovation &
collaboration platform, to enhance tech-for-good information
sharing / transparency, learning, exchange and accelerate
collaboration among tech for good ecosystem players.

> In a modern world, **developers** are akin to the **carpenters, blacksmiths and workers** of older times; developing and building to improve everyday life  
>
> Hence, we've named our project after *Hephaestus*, the Greek God of craftsmen

Our solution intends to be a platform where users can freely join, chat with other developers, forum communities, plan their projects, all the while exploring a myriad of problem statements  
They may then submit a solution proposal through the platform, which is vetted. If accepted, they get their own section of the server dedicated to showcasing their work, and may through this section promote the work further to invite other developers to collaborate on the project

# Main Components

There are 3 main components to the project
## Main Website

The Main Website will be the landing page for this project

It will showcase
- About us information
- Trending approved projects
- Latest social problem

It is able to interface with our other components to fetch up-to-date data; such that when new projects are proposed and accepted, it is immediately reflected on the website as well

> **Technologies**:  
> React
***
## Mattermost Server

A Discord-like, self-hostable platform for chatting and collaboration. We use its heavy integration support to create bots and commands that aid in supporting such a community. It can host multiple "Teams", each Team being a small group of channels where individuals may chat, voice call, and share freely. It consists of:

- One main Team to find out about current projects, problem statements, and to learn more about SIP
- One other Team to submit project ideas/proposals, side-by-side with a Playbook feature that will inform users of the requirements
- If a user's submission is accepted, they get their own Team channel to host their project, and 

> **Technologies**:  
> Cloud Hosting (DigitalOceans)   
> Firebase (Firestore and Storage)  
> - Firestore to store problem statement submissions
> - Storage to store photos and other files submitted by users

### Benefits over similar platforms like Discord
- All servers are collected at one point and can be freely viewed & joined to learn more about the project
- Heavily integratable, allowing for more interactions with the user and platform
- Self-hosted and infinitely more customizeable
***
## Admin Dashboard w/ API
A admin-only web dashboard that visualizes the happenings on the Mattermost server. 

- Lists all project proposals submitted and allows for approval. Once approved, the user is automatically notified. Admins can then set the user up with a Team, and other resources, to get them started
- Allows for managing of problem statements