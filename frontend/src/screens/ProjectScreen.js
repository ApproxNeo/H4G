import React from "react";
import ItemRow from "../components/ItemRow";

export default function ProjectScreen() {
    const dummy = [
        {
            "theme": "bloom",
            "desc": "bloom belives that every woman deserves a role of growth",
            "imgLink": "https://d112y698adiu2z.cloudfront.net/photos/production/software_thumbnail_photos/001/871/512/datas/medium.jpg",
        },
        {
            "theme": "Habitat Heroes",
            "desc": "Build homes, communities and hope through a virtual house-building",
            "imgLink": "https://d112y698adiu2z.cloudfront.net/photos/production/software_thumbnail_photos/001/871/372/datas/medium.png",
        },
        {
            "theme": "Seek&Send",
            "desc": "Utilising technology in bringing Social Enterprises closer together so they may forge a community to exchange knowledge and skills with one another.",
            "imgLink": "https://d112y698adiu2z.cloudfront.net/photos/production/software_thumbnail_photos/001/869/206/datas/medium.png",
        },
    ]
    return (
        <div style={{
            flex: 1,
            display: "flex",
            padding:"48px calc((100% - 800px)/2)",
            flexWrap: 'wrap',
            gap: "30px",
            justifyContent: "center"
        }}>           
            {dummy.map((item, index) => <ItemRow key={index} item={item}/>)}
        </div>
      );
}