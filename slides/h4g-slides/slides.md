---
# try also 'default' to start simple
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://source.unsplash.com/collection/94734566/1920x1080
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# show line numbers in code blocks
lineNumbers: false
# some information about the slides, markdown enabled
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# persist drawings in exports and build
drawings:
  persist: false
# page transition
transition: slide-left
# use UnoCSS
css: unocss
---

# Hephaestus

A collaboration platform for tech4good developers



<div class="text-sm">

> *In a modern world, **developers** are akin to the **carpenters, blacksmiths and workers**   
> of older times; developing and building to improve everyday life*
> 
> *Hence, we've named our project after *Hephaestus*, the Greek God of craftsmen*  
> "  
> Christopher Tan, Clement Neo
</div>

<br>

<div class="text-left">



</div>


<div class="abs-br m-6 flex gap-2">
  <b>Links!</b>
  <a href="https://hephaestus.approxneo.me" target="_blank" alt="GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:view />
  </a>
  <a href="https://github.com/approxneo/h4g" target="_blank" alt="GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
transition: fade-out
---
# Chosen Problem Statement
> Develop and design a global tech-for-good innovation & collaboration platform, to enhance tech-for-good information sharing / transparency, learning, exchange and accelerate collaboration among tech for good ecosystem players

<br/>

# Pain Point
> In the current setup, there is a disconnect **between fellow Developers**, and **between the Developers and Organisations**
> - Between fellow Developers, there is no platform to discuss ideas and to share freely on what they have ideated
> - Between Developers and Organisations, Developers simply pose ideas which are either accepted or rejected by Organisaions

<br/>

---
transition: fade-out
---
# Our Solution
> Provide a platform where users can freely chat, voice call and share ideas all the while trying to solve complex world problems together

We propose a platform for people to
- Learn about social issues to work on and innovative solutions
- Propose innovative ideas or find like-minded teammates with the technical competencies
- Have their ideas follow a stringent minimum requirement or learn how to start a project
- Projects with potential are promoted and can be mentored

---
transition: fade-out
---
# Impact

### Novelty

- 🚅 Speed of collaboration - devs can hop onto the platform to learn more about the trending social projects
- 🤼 devs can find like minded teammates with the required technical competency or expertise
- 🧫 Culture of innovation - devs can bring and share radically different ideas

<br>

### Automation
- Streamline the project proposal submission process
- Allow for pledging, event submission, and act as a T4G directory
- Give approved projects a 'home page' as well as a platform to start a community and attract others to contribute

---
transition: fade-out
layout: two-cols
---
# Main Components

### Landing Page

- About us information
- Trending approved projects
- Latest social problem

<img src="frontend.png" class="rounded  border-gray-500 absolute right-5 top-20 h-30">

<br/>

### Admin Page
- admin-only web dashboard
- Lists all project proposals submitted
- Allows for managing of problem statements

<img src="admin.png" class="rounded  border-gray-500 absolute right-5 bottom-10">



::right::

<br>

### Mattermost Server

<div class="text-sm">

- A Discord-like, self-hostable platform for chatting and collaboration
- has heavy integration support to create bots and commands that aid in supporting such a community
- can host multiple "Teams", each Team being a small group of channels where individuals may chat, voice call, and share freely
</div>

<img src="mm_welcome.png" class="rounded  border-gray-500 absolute bottom-0">



---
transition: fade-out
---
# Demo

1. Users can visit the landing page to get to Mattermost
2. Once they create an account, they are given a welcome message  
 to describe the server, and its capabilities
3. From here, users may:
  - Read the rules
  - Find out more about SIP
  - Read the available problem statements
  - Read the existing solutions being  
    developed

<img src="login.png" class="rounded  border-gray-500 absolute top-5 right-0 w-100">
<img src="welcome.png" class="rounded  border-gray-500 absolute top-50 right-0 w-140">

---
transition: fade-out
---
# Demo - Using Mattermost 
1. Mattermost can be used to chat, send files and voice call
2. It has in-depth formatting, allowing for in-channel sharing of code, LaTeX formulae etc

<img src="usage.png" class="rounded  border-gray-500 absolute top-50 right-0 w-140">

---
transition: fade-out
---
# Demo - View Projects
1. In the `solutions` channel, users can view the existing projects, adding a "like" to them if wanted
2. To learn more, users can click into the project to be invited into the Project's Team

<br><br><br><br><br><br><br><br><br>

> Each icon is a Team, with one main Team,  
> and the resting being Teams hosting the   
> various other approved projects

<img src="demo1.png" class="rounded  border-gray-500 absolute top-50 right-0 w-160">

<img src="demo2.png" class="rounded  border-gray-500 absolute top-50 left-20 w-50">


---
transition: fade-out
---
# Demo - Submit Proposals
1. By heading to the Submissions Team, users can start a "Playbook" to initiate the submission process
2. A channel will be created for them, with a Playbook on the side. This contains a checklist of what to prepare
3. Once prepared, users can use the `/submit` command to fill in a form for their proposal, on Mattermost itself

<br><br><br><br><br><br><br><br><br>

4. This submission is then show on the admin dashboard, to be evaluated. Admins may also chat with the user on Mattermost to get a better idea of their submission

<img src="playbk.png" class="rounded  border-gray-500 absolute top-50 left-10 h-60">
<img src="check.png" class="rounded  border-gray-500 absolute top-50 right-70 h-68">
<img src="submit.png" class="rounded  border-gray-500 absolute top-50 right-10 h-68">

---
transition: fade-out
---

# How we built it
- Frontend with React, HTML and CSS
- Backend with Flask and Firebase
- Collaboration platform with Mattermost
- Hosted on DigitalOceans

---
layout: cover
---
# End