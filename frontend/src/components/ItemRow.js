import React from "react";

export default function ItemRow({ item }) {
    return (
        <div style={{
            display: "flex",
            border: "1px solid #ccc",
            width: "360px",
            height: "400px",
            padding: "20px",
            flexDirection: "column",
            alignItems: "center"
        }}>
            <img
                src={item.imgLink}
                alt="new"
                width="280px"
                height="140px"
            />
            <h1>{item.theme}</h1>
            <p>{item.desc}</p>
        </div>
    );
}
