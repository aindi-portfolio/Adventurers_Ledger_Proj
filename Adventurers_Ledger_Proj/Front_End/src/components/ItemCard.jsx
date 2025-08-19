import React from "react";

const ItemCard = ({ item }) => {
  return (
    <div className="item bg-yellow-100 p-4 rounded shadow w-64">
      <strong className="text-yellow-800 block mb-2 text-center">{item.name}</strong>
      <p className="text-sm text-gray-700 line-clamp-3">{item.description ? `Description: ${item.description}`:null}</p>
      <p className=" font-semibold text-yellow-900">Price: {item.cost_amount} {item.cost_unit}</p>
      <div className="flex justify-center mt-2">
      <button className=" bg-yellow-500 text-white px-4 py-2 rounded hover:bg-yellow-600 transition-colors">Buy</button>
      <button className=" bg-yellow-300 text-yellow-800 px-4 py-2 rounded hover:bg-yellow-400 transition-colors">Sell</button>
      </div>
    </div>
  );
};

export default ItemCard;
