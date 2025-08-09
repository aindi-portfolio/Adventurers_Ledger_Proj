import React from "react";

export default function ItemBox({ item, onClick }) {
  return (
    <div className="item-box" onClick={() => onClick(item)}>
      <img src={item.image} alt={item.name} className="item-image" />
      <div className="item-details">
        <h3 className="item-name">{item.name}</h3>
        <p className="item-description">{item.description}</p>
        <p className="item-price">Price: {item.price} gold</p>
      </div>
    </div>
  );
}