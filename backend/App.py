from init import *
from flask import jsonify, request
from shared.bots import *
import requests
from attachments import *

app = create_app()
app.debug = True


@app.route("/solutions")
def solutions():
    return jsonify(
        [
            {
                "name": "bloom",
                "desc": "bloom belives that every woman deserves a role of growth",
                "imgLink": "https://d112y698adiu2z.cloudfront.net/photos/production/software_thumbnail_photos/001/871/512/datas/medium.jpg",
            },
            {
                "name": "Habitat Heroes",
                "desc": "Build homes, communities and hope through a virtual house-building",
                "imgLink": "https://d112y698adiu2z.cloudfront.net/photos/production/software_thumbnail_photos/001/871/372/datas/medium.png",
            },
            {
                "name": "Seek&Send",
                "desc": "Utilising technology in bringing Social Enterprises closer together so they may forge a community to exchange knowledge and skills with one another.",
                "imgLink": "https://d112y698adiu2z.cloudfront.net/photos/production/software_thumbnail_photos/001/869/206/datas/medium.png",
            },
        ]
    )


@app.route("/problems")
def problems():
    return jsonify(
        [
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
    )


@app.route("/solutions", methods=["post"])
def solutions_post():
    response1 = requests.post(
        url="https://hephaestus.approxneo.me/plugins/playbooks/api/v0/runs",
        headers=headers,
        json={
            "name": "Malware Intrusion on Microsoft Teams Cloud",
            "description": "There is one server in the EU cluster that is not responding since April 12.",
            "owner_user_id": request.form.get("user_id"),
            "team_id": "9n7s7qj4ttbgmmh9hunryoph5h",
            "playbook_id": "fp8xmgq4rbfpd8pdrm8wikt6ea",
        },
    )


@app.route("/submit", methods=["post"])
def solutions_submit():
    bot.integration_actions.open_dialog(
        options=drill_attachment(request.form.get("trigger_id"))
    )
    return jsonify({"success": True})


@app.route("/submit/dialog", methods=["post"])
def solutions_submit_dialog():
    bot.posts.create_post(
        options={
            "channel_id": request.form.get("channel_id"),
            "message": "Thanks!",
            "props": dialog_submission(),
        }
    )
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
