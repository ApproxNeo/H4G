import React from "react";

export default function ProjectRow({ item }) {
  return (
    <div style={{
        border: "1px solid #ccc",
        borderRadius: "5px",
        padding: "20px",
        margin: "1rem 0",
    }}>
        <h1>{item.theme}</h1>
        <p>{item.desc}</p>
    </div>
  );
}
