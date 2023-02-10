def INCIDENT_ELEMENT(case_no, team_id):
    return [
        {
            "fallback": "test",
            "color": "#FF0000",
            "text": "The injects for case {} have been sent out through email.".format(
                case_no + 1
            ),
            "author_name": "ACID Drill",
            "author_icon": "https://mattermost.com/wp-content/uploads/2022/02/icon_WS.png",
            "author_link": "https://mattermost.org/",
            "title": "First injects have been sent out",
            "title_link": "https://developers.mattermost.com/integrate/reference/message-attachments/",
            "fields": [
                {
                    "short": False,
                    "title": "Actions required",
                    "value": "Verify that you have received the injects",
                },
            ],
            "actions": [
                {
                    "id": "message",
                    "name": "Yes, received",
                    "integration": {
                        "url": "http://mm.space.approxneo.me:9000/drills/received/{}/{}".format(
                            team_id, case_no
                        ),
                        "context": {"action": "do_something_ephemeral"},
                    },
                },
                {
                    "id": "update",
                    "name": "Did not receive",
                    "integration": {
                        "url": "http://mm.space.approxneo.me:9000/drills/not_received/{}/{}".format(
                            team_id, case_no
                        ),
                        "context": {"action": "do_something_update"},
                    },
                },
            ],
        }
    ]


def RECEIVED_ELEMENT(case_no):
    return [
        {
            "fallback": "test",
            "color": "#FF0000",
            "text": "The injects for case {} have been sent out through email.".format(
                case_no + 1
            ),
            "author_name": "ACID Drill",
            "author_icon": "https://mattermost.com/wp-content/uploads/2022/02/icon_WS.png",
            "author_link": "https://mattermost.org/",
            "title": "First injects have been sent out",
            "title_link": "https://developers.mattermost.com/integrate/reference/message-attachments/",
            "fields": [
                {
                    "short": False,
                    "title": "Actions required",
                    "value": "Verify that you have received the injects",
                },
                {
                    "short": True,
                    "title": "Inject Received",
                    "value": "Inject has been received",
                },
            ],
        }
    ]


def NOT_RECEIVED_ELEMENT(case_no):
    return [
        {
            "fallback": "test",
            "color": "#FF0000",
            "text": "The injects for case {} have been sent out through email.".format(
                case_no
            ),
            "author_name": "ACID Drill",
            "author_icon": "https://mattermost.com/wp-content/uploads/2022/02/icon_WS.png",
            "author_link": "https://mattermost.org/",
            "title": "First injects have been sent out",
            "title_link": "https://developers.mattermost.com/integrate/reference/message-attachments/",
            "fields": [
                {
                    "short": False,
                    "title": "Actions required",
                    "value": "Verify that you have received the injects",
                },
                {
                    "short": True,
                    "title": "Inject NOT received",
                    "value": "You have indicated that you did not receive the case 1 injects, please hold while a operator re-sends the injects",
                },
            ],
        }
    ]


def welcome_msg():
    return {
        "attachments": [
            {
                "fallback": "Welcome Message",
                "color": "#9933ff",
                "text": "The Hephaestus Mattermost Server is a collaborative platform for developers to come together and strive to solve salient world problems. Here, we promote using Tech 4 Good to educate, empower, and enhance a new generation of conscious leaders to apply technology for greater good. This is where the world’s best technologists, entrepreneurs, and investors unite to turn large global challenges into growth opportunities and solve the biggest challenges of our time.",
                "author_name": "Hesphaestus",
                "author_icon": "http://www.mattermost.org/wp-content/uploads/2016/04/icon_WS.png",
                "author_link": "#",
                "title": "Welcome to Hephaestus",
                "title_link": "#",
                "fields": [
                    {
                        "short": False,
                        "title": "Things to do",
                        "value": "Feel free to treat this server like a lounge, and chat with other developers freely. You may also:",
                    },
                    {
                        "short": True,
                        "title": "Read the Rules",
                        "value": "Please adhere to our simple set of [Rules](https://hephaestus.approxneo.me/hephaestus/channels/rules)",
                    },
                    {
                        "short": True,
                        "title": "About Us",
                        "value": "Find out more [About Us]()",
                    },
                    {
                        "short": True,
                        "title": "Read the Problem Statements",
                        "value": "Found [here]()",
                    },
                    {
                        "short": True,
                        "title": "Find out about the solutions proposed",
                        "value": "Visit [this channel]()",
                    },
                ],
                "image_url": "https://i.imgur.com/ET6P3XO.png",
            }
        ]
    }


def solution_msg():
    return {
        "attachments": [
            {
                "fallback": "Solution Submission Message",
                "color": "#9933ff",
                "text": "Think you have what it takes to solve some of the world's biggest problem? Send in your proposals for evaluation now!",
                "author_name": "Hesphaestus",
                "author_icon": "http://www.mattermost.org/wp-content/uploads/2016/04/icon_WS.png",
                "author_link": "#",
                "title": "Submit Solution Proposal",
                "title_link": "#",
                "fields": [
                    {
                        "short": False,
                        "title": "Requirements",
                        "value": "Project Ideation, Technologies employed and ",
                    },
                    {
                        "short": True,
                        "title": "How to submit",
                        "value": 'Open the clipboard at the top-right, and click `run` on the "Project Proposal Submission" Playbook',
                    },
                    {
                        "short": True,
                        "title": "Benefits",
                        "value": "Get your own Team channel to attract other developers to work on the project together, acting as a home page for your proposal. ",
                    },
                ],
                "image_url": "https://i.imgur.com/ET6P3XO.png",
            }
        ]
    }


def solution1():
    return {
        "attachments": [
            {
                "fallback": "bloom",
                "color": "#9933ff",
                "text": "bloom belives that every woman deserves a role of growth",
                "author_name": "Bloom",
                "author_icon": "http://www.mattermost.org/wp-content/uploads/2016/04/icon_WS.png",
                "author_link": "#",
                "title": "The Bloom Project",
                "title_link": "#",
                "fields": [
                    {
                        "short": False,
                        "title": "Project Description",
                        "value": "To improve social mobility among low-income women, employment is a key consideration. There is a white space in today's landscape, where current job boards do not adequately consider soft skills and disadvantage our target audience of low-income women, and current initiatives for the target audience are not sufficient in supporting the long-term employment of these women. Thus, our project was formed.",
                    },
                    {
                        "short": True,
                        "title": "Visit Project Team",
                        "value": "[bloom Team](https://hephaestus.approxneo.me/bloom)",
                    },
                    {
                        "short": True,
                        "title": "Visit Project Website",
                        "value": "[bloom]()",
                    },
                ],
                "image_url": "https://d112y698adiu2z.cloudfront.net/photos/production/software_thumbnail_photos/001/871/512/datas/medium.jpg",
                "actions": [
                    {
                        "id": "message",
                        "name": "Likes - 17 ♥",
                        "integration": {
                            "url": "http://127.0.0.1:7357",
                            "context": {"action": "do_something_ephemeral"},
                        },
                    },
                ],
            }
        ]
    }


def solution2():
    return {
        "attachments": [
            {
                "fallback": "Habitat Heroes",
                "color": "#9933ff",
                "text": "Build homes, communities, and hope through a virtual house-building game that mirrors the experience of physical volunteering programs.",
                "author_name": "Habitat Heroes",
                "author_icon": "http://www.mattermost.org/wp-content/uploads/2016/04/icon_WS.png",
                "author_link": "#",
                "title": "Habitat Heroes Project",
                "title_link": "#",
                "fields": [
                    {
                        "short": False,
                        "title": "Project Description",
                        "value": "We found Habitat for Humanity’s problem statement to be the most relatable, since most of us have had experience volunteering overseas and helping with similar projects, where we helped to build homes, communities, and hope. We were thus inspired by the extensive efforts of Habitat for Humanity in building homes for underprivileged communities worldwide. One could only imagine our dismay when we heard about how the pandemic affected these efforts and initiatives.",
                    },
                    {
                        "short": True,
                        "title": "Visit Project Team",
                        "value": "[Habitat Heroes Team](https://hephaestus.approxneo.me/habitat-heroes)",
                    },
                    {
                        "short": True,
                        "title": "Visit Project Website",
                        "value": "[Habitat Heroes]()",
                    },
                ],
                "image_url": "https://d112y698adiu2z.cloudfront.net/photos/production/software_thumbnail_photos/001/871/372/datas/medium.png",
                "actions": [
                    {
                        "id": "message",
                        "name": "Likes - 9",
                        "integration": {
                            "url": "http://127.0.0.1:7357",
                            "context": {"action": "do_something_ephemeral"},
                        },
                    },
                ],
            }
        ]
    }


def solution3():
    return {
        "attachments": [
            {
                "fallback": "Seek&Send",
                "color": "#9933ff",
                "text": "Utilising technology in bringing Social Enterprises closer together so they may forge a community to exchange knowledge and skills with one another.",
                "author_name": "Seek&Send",
                "author_icon": "http://www.mattermost.org/wp-content/uploads/2016/04/icon_WS.png",
                "author_link": "#",
                "title": "Seek&Send Project",
                "title_link": "#",
                "fields": [
                    {
                        "short": False,
                        "title": "Project Description",
                        "value": "COVID-19 has generated social, economic and health issues globally, overwhelming current healthcare institutions and governmental organisations, thus creating the need for more social enterprises (SE) to address social needs. However, these SEs need support, since they face major challenges. We created Seek&Send in order to address these challenges by creating a support system via a forum, where SEs can exchange information with one another.",
                    },
                    {
                        "short": True,
                        "title": "Visit Project Team",
                        "value": "[Seek&Send Team](https://hephaestus.approxneo.me/seeksend)",
                    },
                    {
                        "short": True,
                        "title": "Visit Project Website",
                        "value": "[Seek&Send]()",
                    },
                ],
                "image_url": "https://d112y698adiu2z.cloudfront.net/photos/production/software_thumbnail_photos/001/869/206/datas/medium.png",
                "actions": [
                    {
                        "id": "message",
                        "name": "Likes - 11",
                        "integration": {
                            "url": "http://127.0.0.1:7357",
                            "context": {"action": "do_something_ephemeral"},
                        },
                    },
                ],
            },
        ]
    }


def drill_attachment(
    trigger_id,
):
    return {
        "trigger_id": "{}".format(trigger_id),
        "url": "http://mm.space.approxneo.me:9000/submit/dialog",
        "dialog": {
            "callback_id": "1",
            "title": "Submit Project Proposal",
            "introduction_text": "Submit a project proposal based off of one of the provided problem statements",
            "elements": [
                {
                    "display_name": "Proposed Name",
                    "name": "project_name",
                    "type": "text",
                },
                {
                    "display_name": "Problem Statement",
                    "name": "problem_statement",
                    "type": "select",
                    "options": [
                        {"text": "Statement 001", "value": "opt1"},
                        {"text": "Statement 002", "value": "opt2"},
                        {"text": "Statement 003", "value": "opt3"},
                    ],
                },
                {
                    "display_name": "Project Description",
                    "name": "desc",
                    "type": "textarea",
                },
                {
                    "display_name": "Technologies & Nature of Project",
                    "name": "tech",
                    "type": "textarea",
                },
                {
                    "display_name": "Past experiences and Portfolio",
                    "name": "expr",
                    "type": "textarea",
                },
            ],
            "submit_label": "Submit",
            "notify_on_cancel": False,
            "state": "<string provided by the integration that will be echoed back with dialog submission>",
        },
    }

def dialog_submission():
    return {
        "attachments": [
            {
                "fallback": "Dialog Submissions",
                "color": "#9933ff",
                "text": "Thank you for your proposal! Our team will evaluate it and get back to you. Do stay tuned on this channel as there may be further questions posted to get a better understanding of your ideation",
                "author_name": "Hephaestus",
                "author_icon": "http://www.mattermost.org/wp-content/uploads/2016/04/icon_WS.png",
                "author_link": "#",
                "title": "Project Proposal Submission",
                "title_link": "#",
                "actions": [
                    {
                        "id": "message",
                        "name": "Edit Proposal",
                        "integration": {
                            "url": "http://127.0.0.1:7357",
                            "context": {"action": "do_something_ephemeral"},
                        },
                    },
                ],
            },
        ]
    }